from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from antlr4.tree.Trees import Trees
def main():
    
    # ورودی فایل برای lexer
    input_stream = FileStream("C:/Users/Lenovo/Desktop/compiler/CProject1/grammer/input.mc", encoding='utf-8')

    # ساخت lexer و parser
    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)

    # ساخت درخت نحو
    tree = parser.program()

    # نمایش درخت در کنسول (متنی)
    print(tree.toStringTree(recog=parser))