import jaro
import sys
import os.path
import antlr4
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

sys.path.append(os.path.dirname(__file__))
from GQLLexer import GQLLexer
from GQLParser import GQLParser


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(
            "ERROR: when parsing line %d column %d: %s\n" % (line, column, msg)
        )


class GrammarEvaluator:
    def evaluate(self, query_predict, query_gold):
        error_listener = MyErrorListener()
        try:
            input_stream = InputStream(query_gold)
            lexer = GQLLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            stream = CommonTokenStream(lexer)
            parser = GQLParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            tree = parser.gqlProgram()
            try:
                input_stream = InputStream(query_predict)
                lexer = GQLLexer(input_stream)
                lexer.removeErrorListeners()
                lexer.addErrorListener(error_listener)
                stream = CommonTokenStream(lexer)
                parser = GQLParser(stream)
                parser.removeErrorListeners()
                parser.addErrorListener(error_listener)
                tree = parser.gqlProgram()
                return 1
            except Exception as e:
                return 0
        except Exception as e:
            return -1
