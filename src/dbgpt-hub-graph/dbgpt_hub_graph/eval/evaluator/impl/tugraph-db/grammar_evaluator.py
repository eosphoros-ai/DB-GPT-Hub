import jaro

class GrammarEvaluator:

    def evaluate(self, query_predict, query_gold):
        return jaro.jaro_winkler_metric(query_predict, query_gold)