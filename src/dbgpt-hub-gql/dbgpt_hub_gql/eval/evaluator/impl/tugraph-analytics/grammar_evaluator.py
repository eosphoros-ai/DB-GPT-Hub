import jpype
import os.path


class GrammarEvaluator:
    def __init__(self):
        jvmPath = jpype.getDefaultJVMPath()

        # gql grammar paerser from tugraph-analytics https://github.com/TuGraph-family/tugraph-analytics/tree/master/geaflow/geaflow-dsl/geaflow-dsl-parser/src/main/java/com/antgroup/geaflow/dsl/parser
        jarpath = (
            os.path.dirname(__file__)
            + "/geaflow-dsl-parser-0.5.0-jar-with-dependencies.jar"
        )
        jvm_cp = f"-Djava.class.path={jarpath}"
        jpype.startJVM(jvmPath, "-ea", classpath=[jarpath], convertStrings=False)
        JDClass = jpype.JClass("com.antgroup.geaflow.dsl.parser.GeaFlowDSLParser")
        self.jd = JDClass()

    def evaluate(self, query_predict, query_gold, db_id):
        try:
            result_gold = self.jd.parseStatement(query_gold)
            try:
                result_predict = self.jd.parseStatement(query_predict)
                return 1
            except jpype.JException as e_query:
                return 0
        except jpype.JException as e_gold:
            return -1
