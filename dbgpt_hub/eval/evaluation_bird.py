"""
do evaluate about the predict sql in dataset BIRD,compare with default dev.sql
--db
"""
import sys
import json
import argparse
import sqlite3
import multiprocessing as mp
from func_timeout import func_timeout, FunctionTimedOut
import math
import time


def load_json(dir):
    with open(dir, "r") as j:
        contents = json.loads(j.read())
    return contents


def result_callback(result):
    exec_result.append(result)


def execute_sql(predicted_sql, ground_truth, db_path):
    conn = sqlite3.connect(db_path)
    # Connect to the database
    cursor = conn.cursor()
    pred_start_time = time.time()
    cursor.execute(predicted_sql)
    pred_exec_time = time.time() - pred_start_time
    predicted_res = cursor.fetchall()
    true_start_time = time.time()
    cursor.execute(ground_truth)
    true_exec_time = time.time() - true_start_time
    ground_truth_res = cursor.fetchall()
    res = 0
    time_ratio = 0
    if set(predicted_res) == set(ground_truth_res):
        res = 1
        time_ratio = true_exec_time/pred_exec_time if pred_exec_time > 0 else 0
    return res, time_ratio


def execute_model(predicted_sql, ground_truth, db_place, idx, meta_time_out):
    try:
        res, time_ratio = func_timeout(meta_time_out, execute_sql,
                           args=(predicted_sql, ground_truth, db_place))
    except KeyboardInterrupt:
        sys.exit(0)
    except FunctionTimedOut:
        result = [(f"timeout",)]
        res = 0
        time_ratio = 0
    except Exception as e:
        result = [(f"error",)]  # possibly len(query) > 512 or not executable
        res = 0
        time_ratio = 0
    # print(result)
    # result = str(set([ret[0] for ret in result]))
    result = {"sql_idx": idx, "res": res, "match": int(predicted_sql == ground_truth), "time_ratio": time_ratio}
    # print(result)
    return result


def package_sqls(sql_path, db_root_path, mode="gpt", data_mode="dev"):
    clean_sqls = []
    db_path_list = []
    if mode == "gpt":
        # sql_data = json.load(open(sql_path + 'predict_' + data_mode + '.json', "r'))
        # for idx, sql_str in sql_data.items():
        #     if type(sql_str) == str:
        #         sql, db_name = sql_str.split('\t----- bird -----\t')
        #     else:
        #         sql, db_name = " ", "financial"
        #     clean_sqls.append(sql)
        #     db_path_list.append(db_root_path + db_name + '/' + db_name + '.sqlite')
        with open(sql_path) as f:
            for l in f.readlines():
                # if len(l.strip()) == 0:
                #     sql, db_name = " ", "financial"
                # else:
                #     sql, db_name = l.split('\t')
                clean_sqls.append(l.strip())
                # db_path_list.append(db_root_path + db_name + '/' + db_name + '.sqlite')
    elif mode == "gt":
        sqls = open(sql_path)
        sql_txt = sqls.readlines()
        # sql_txt = [sql.split('\t')[0] for sql in sql_txt]
        for idx, sql_str in enumerate(sql_txt):
            sql, db_name = sql_str.strip().split("\t")
            clean_sqls.append(sql)
            db_path_list.append(db_root_path + db_name + "/" + db_name + ".sqlite")

    return clean_sqls, db_path_list


def run_sqls_parallel(sqls, db_places, num_cpus=1, meta_time_out=30.0):
    pool = mp.Pool(processes=num_cpus)
    for i, sql_pair in enumerate(sqls):
        predicted_sql, ground_truth = sql_pair
        pool.apply_async(
            execute_model,
            args=(predicted_sql, ground_truth, db_places[i], i, meta_time_out),
            callback=result_callback,
        )
    pool.close()
    pool.join()


def sort_results(list_of_dicts):
    return sorted(list_of_dicts, key=lambda x: x["sql_idx"])


def compute_ves(exec_results):
    num_queries = len(exec_results)
    total_ratio = 0
    count = 0

    for i, result in enumerate(exec_results):
        if result["time_ratio"] != 0:
            count += 1
        total_ratio += math.sqrt(result["time_ratio"]) * 100
    ves = (total_ratio/num_queries)
    return ves



def compute_acc_by_diff(exec_results, diff_json_path, metric):
    num_queries = len(exec_results)
    results = [res[metric] for res in exec_results]
    contents = load_json(diff_json_path)
    simple_results, moderate_results, challenging_results = [], [], []

    for i, content in enumerate(contents):
        if content["difficulty"] == "simple":
            simple_results.append(exec_results[i])

        if content["difficulty"] == "moderate":
            moderate_results.append(exec_results[i])

        if content["difficulty"] == "challenging":
            challenging_results.append(exec_results[i])
    if metric in ["res", "match"]:
        simple_acc = sum([res[metric] for res in simple_results]) / len(simple_results)
        moderate_acc = sum([res[metric] for res in moderate_results]) / len(moderate_results)
        challenging_acc = sum([res[metric] for res in challenging_results]) / len(challenging_results)
        all_acc = sum(results) / num_queries
    elif metric in ["time_ratio"]:
        simple_acc = compute_ves(simple_results)
        moderate_acc = compute_ves(moderate_results)
        challenging_acc = compute_ves(challenging_results)
        all_acc = compute_ves(exec_results)
    else:
        raise NotImplementedError(f"metric: {metric} is not supported")
    count_lists = [len(simple_results), len(moderate_results), len(challenging_results), num_queries]
    if metric in ["res", "match"]:
        return simple_acc * 100, moderate_acc * 100, challenging_acc * 100, all_acc * 100, count_lists
    else:
        return simple_acc, moderate_acc, challenging_acc, all_acc, count_lists


def print_data(score_lists, count_lists, metric="Exec ACCURACY"):
    levels = ["simple", "moderate", "challenging", "total"]
    print("{:20} {:20} {:20} {:20} {:20}".format("", *levels))
    print("{:20} {:<20} {:<20} {:<20} {:<20}".format('count', *count_lists))

    print(f'====================================== {metric} =====================================')
    print("{:20} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}".format("accuracy", *score_lists))


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--predicted_sql_path", type=str, default="../../pred_sql/pred_sql_bird_qwen14b_1212.sql")
    args_parser.add_argument("--ground_truth_path", type=str, default="../../dbgpt_hub/data/bird/dev/dev.sql")
    args_parser.add_argument("--data_mode", type=str, default="dev")
    args_parser.add_argument("--db_root_path", type=str, default="../../dbgpt_hub/data/bird/dev/dev_databases/")
    args_parser.add_argument("--num_cpus", type=int, default=1)
    args_parser.add_argument("--meta_time_out", type=float, default=30.0)
    args_parser.add_argument("--mode_gt", type=str, default="gt")
    args_parser.add_argument("--mode_predict", type=str, default="gpt")
    args_parser.add_argument("--difficulty", type=str, default="simple")
    args_parser.add_argument("--diff_json_path", type=str, default="")
    args_parser.add_argument("--etype", dest="etype", type=str, default="match", choices=("all", "exec", "match", "ves"),)

    args = args_parser.parse_args()
    exec_result = []

    pred_queries, db_paths = package_sqls(args.predicted_sql_path, args.db_root_path, mode=args.mode_predict,
                                          data_mode=args.data_mode)
    # generate gt sqls:
    gt_queries, db_paths_gt = package_sqls(args.ground_truth_path, args.db_root_path, mode="gt",
                                           data_mode=args.data_mode)

    if len(db_paths) == 0:
        db_paths = db_paths_gt

    query_pairs = list(zip(pred_queries, gt_queries))
    if args.etype in ["all", "exec", "ves"]:
        run_sqls_parallel(query_pairs, db_places=db_paths, num_cpus=args.num_cpus, meta_time_out=args.meta_time_out)
    else:
        for i, sql_pair in enumerate(query_pairs):
            predicted_sql, ground_truth = sql_pair
            exec_result.append({"sql_idx": i, "match": int(predicted_sql == ground_truth)})
    exec_result = sort_results(exec_result)

    print("start calculate")
    if args.etype in ["all", "exec"]:
        simple_acc, moderate_acc, challenging_acc, acc, count_lists = \
            compute_acc_by_diff(exec_result, args.diff_json_path, "res")
        score_lists = [simple_acc, moderate_acc, challenging_acc, acc]
        print_data(score_lists, count_lists, metric="Exec Accuracy")
    if args.etype in ["all", "match"]:
        simple_acc, moderate_acc, challenging_acc, acc, count_lists = \
            compute_acc_by_diff(exec_result, args.diff_json_path, "match")
        score_lists = [simple_acc, moderate_acc, challenging_acc, acc]
        print_data(score_lists, count_lists, metric="Match Accuracy")
    if args.etype in ["all", "ves"]:
        simple_acc, moderate_acc, challenging_acc, acc, count_lists = \
            compute_acc_by_diff(exec_result, args.diff_json_path, "time_ratio")
        score_lists = [simple_acc, moderate_acc, challenging_acc, acc]
        print_data(score_lists, count_lists, metric="Ves")
    print(
        "==========================================================================================="
    )
    print("Finished evaluation")
