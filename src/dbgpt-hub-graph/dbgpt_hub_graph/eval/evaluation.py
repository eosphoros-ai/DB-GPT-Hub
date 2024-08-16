import os
import sys
import argparse
import importlib
from evaluator.evaluator import Evaluator
from evaluator.similarity_evaluator import SimilarityEvaluator

def evaluate(gold, predict, etype, impl):
    # log_file = open("detail.log", "w")

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

    print(f"gseq_one length  {len(gseq_one)}")
    print(f"pseq_one length {len(pseq_one)}")
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
        # print(score)
        # print(pseq_one[i])
        # print(gseq_one[i])
        # print("--------------------------------------")
    print(score_total / total)

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

    # Second, evaluate the predicted SQL queries
    evaluate(
        args.gold,
        args.input,
        args.etype,
        args.impl
    )