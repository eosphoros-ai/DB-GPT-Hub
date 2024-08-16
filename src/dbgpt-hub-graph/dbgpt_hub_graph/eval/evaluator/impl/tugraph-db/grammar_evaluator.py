import jaro
import sys
import os.path
import antlr4
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

sys.path.append(os.path.dirname(__file__))
from LcypherLexer import LcypherLexer
from LcypherParser import LcypherParser

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))

class GrammarEvaluator:

    def evaluate(self, query_predict, query_gold):
        error_listener = MyErrorListener()
        try:
            input_stream = InputStream(query_gold)
            lexer = LcypherLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            stream = CommonTokenStream(lexer)
            parser = LcypherParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            tree = parser.oC_Cypher()  # 开始规则
            # print(tree.toStringTree(recog=parser))  # 打印解析树
            try:
                input_stream = InputStream(query_predict)
                lexer = LcypherLexer(input_stream)
                lexer.removeErrorListeners()
                lexer.addErrorListener(error_listener)
                stream = CommonTokenStream(lexer)
                parser = LcypherParser(stream)
                parser.removeErrorListeners()
                parser.addErrorListener(error_listener)
                tree = parser.oC_Cypher()  # 开始规则
                return 1
            except Exception as e:
                return 0
        except Exception as e:
            # print(query_gold)
            # print(e)
            return -1