import jpype
import os.path

class GrammarEvaluator:
    def __init__(self):
        jvmPath = jpype.getDefaultJVMPath()
        jarpath = os.path.dirname(__file__) + "/geaflow-dsl-parser-0.5.0-jar-with-dependencies.jar"
        # deppath = os.path.dirname(__file__) + "/calcite-core-1.18.0-geaflow_1.0.jar"
        
        print(jarpath)
        jvm_cp = f"-Djava.class.path={jarpath}"
        jpype.startJVM(jvmPath, "-ea", classpath=[jarpath], convertStrings=False)
        JDClass = jpype.JClass("com.antgroup.geaflow.dsl.parser.GeaFlowDSLParser")  
        self.jd = JDClass()

    def evaluate(self, query_predict, query_gold):
        try:
            result_gold = self.jd.parseStatement(query_gold)
            # print(f"[PASS]: {result}")
            try:
                result_predict = self.jd.parseStatement(query_predict)
                return 1
            except jpype.JException as e_query:
                return 0
        except jpype.JException as e_gold:
            # print(f"[FAIL]: {query_gold} ------ {e.message}")
            return -1
        