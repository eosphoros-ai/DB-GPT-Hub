import jaro
import antlr4
from antlr4 import *
from evaluator.impl.tugraph_db.Gql.GqlLexer import GqlLexer
from evaluator.impl.tugraph_db.Gql.GqlParser import GqlParser
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))

class GrammarEvaluator:

    def evaluate(self, query_predict, query_gold):
        error_listener = MyErrorListener()
        try:
            input_stream = InputStream(query_gold)
            lexer = GqlLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            stream = CommonTokenStream(lexer)
            parser = GqlParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            tree = parser.gqlRequest()  # 开始规则
            # print(tree.toStringTree(recog=parser))  # 打印解析树
            try:
                input_stream = InputStream(query_predict)
                lexer = GqlLexer(input_stream)
                lexer.removeErrorListeners()
                lexer.addErrorListener(error_listener)
                stream = CommonTokenStream(lexer)
                parser = GqlParser(stream)
                parser.removeErrorListeners()
                parser.addErrorListener(error_listener)
                tree = parser.gqlRequest()  # 开始规则
                return 1
            except Exception as e:
                return 0
        except Exception as e:
            # print(query_gold)
            # print(e)
            return -1