import os
import sys
import argparse
import importlib
import json
import prettytable as pt
from evaluator.evaluator import Evaluator
from evaluator.similarity_evaluator import SimilarityEvaluator

def evaluate(gold, predict, etype, impl):
    log_file = open(f"{os.path.dirname(__file__)}/../output/logs/eval.log", "w")
    log_lines = []

    with open(gold) as f:
        gseq_one = []
        for l in f.readlines():
            if len(l.strip()) == 0:
                # when some predict is none, support it can continue work
                gseq_one.append("no out")
            else:
                gseq_one.append(l.strip())

    
    with open(predict) as f:
        plist = []
        pseq_one = []
        for l in f.readlines():
                if len(l.strip()) == 0:
                    # when some predict is none, support it can continue work
                    pseq_one.append("no out")

                else:
                    pseq_one.append(l.strip())

    assert len(gseq_one) == len(pseq_one), "number of predicted queries and gold standard queries must equal"

    score_total = 0
    if etype == "similarity":
        evaluator = SimilarityEvaluator()
    elif etype == "grammar":
        model_path = f"evaluator.impl.{impl}.grammar_evaluator"
        m = importlib.import_module(model_path)
        GrammarEvaluator = getattr(m, "GrammarEvaluator")
        evaluator = GrammarEvaluator()

    total = 0
    for i in range(len(gseq_one)):
        score = evaluator.evaluate(pseq_one[i], gseq_one[i])
        if score != -1:
            score_total += score
            total += 1
            tmp_log = {}
            tmp_log["pred"] = pseq_one[i]
            tmp_log["gold"] = gseq_one[i]
            tmp_log["score"] = score
            log_lines.append(tmp_log)

    json.dump(log_lines, log_file, ensure_ascii=False, indent=4)

    tb = pt.PrettyTable()
    tb.field_names = ["Evaluation Type", "Total Count", "Accuracy"]
    tb.add_row([etype, len(gseq_one), "{:.3f}".format(score_total / total)])
    print(tb)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        dest="input",
        type=str,
        help="the path to the input file",
        required=True,
    )
    parser.add_argument(
        "--gold", dest="gold", type=str, help="the path to the gold queries", default=""
    )
    parser.add_argument(
        "--etype",
        dest="etype",
        type=str,
        default="similarity",
        help="evaluation type, exec for test suite accuracy, match for the original exact set match accuracy",
        choices=("similarity", "grammar"),
    )
    parser.add_argument(
        "--impl",
        dest="impl",
        type=str,
        default="tugraph-analytics",
        help="implementation folder for grammar evaluator",
    )
    args = parser.parse_args()

    # Print args
    print(f"params as fllows \n {args}")

    # Second, evaluate the predicted GQL queries
    evaluate(
        args.gold,
        args.input,
        args.etype,
        args.impl
    )