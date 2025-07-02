import jaro


class SimilarityEvaluator:
    def evaluate(self, query_predict, query_gold, db_id):
        return jaro.jaro_winkler_metric(query_predict, query_gold)
