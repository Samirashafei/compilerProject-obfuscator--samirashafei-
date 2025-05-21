from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from antlr4.tree.Trees import Trees
def escape_label(text):
    text = text.replace("\\", "\\\\") 
    text = text.replace("\"", "\\\"")  
    text = text.replace("%", "%%")     
    text = text.replace("\n", "\\n")   
    return text

def to_dot(node, parser, counter=[0], parent=None, lines=None):
    
    if lines is None:
        lines = ["digraph ParseTree {"]

    node_id = counter[0]
    counter[0] += 1

    if isinstance(node, TerminalNode):
        label = escape_label(node.getText())
    else:
        label = escape_label(parser.ruleNames[node.getRuleIndex()])

    lines.append(f'  node{node_id} [label="{label}"];')

    if parent is not None:
        lines.append(f'  node{parent} -> node{node_id};')

    for i in range(node.getChildCount()):
        to_dot(node.getChild(i), parser, counter, node_id, lines)

    if parent is None:
        lines.append("}")
        return "\n".join(lines)
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
    # تولید فایل .dot برای Graphviz
    dot_content = to_dot(tree, parser)
    with open("tree.dot", "w", encoding="utf-8") as f:
        f.write(dot_content)

if __name__ == '__main__':
    main()