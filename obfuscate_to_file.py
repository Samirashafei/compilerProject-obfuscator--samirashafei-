from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from ObfuscatorVisitor import ObfuscatorVisitor
import random 
import argparse

def get_random_dead_code():
    return random.choice([
        "int dead_var_{} = {};".format(random.randint(100, 999), random.randint(1000, 9999)),
        "if (0) { printf(\"this will never run\\n\"); }",
        "int unused = {}; unused++;".format(random.randint(1, 100)),
        "char tmp = 'x';",
        "if (1 == 2) { int hidden = 1; }",
        "bool dummy = false;"
    ])
# expression replacment 
def replace_expression_pattern(tokens, i, name_map):
    if i + 2 >= len(tokens):
        return None, 1

    t1, t2, t3 = tokens[i], tokens[i + 1], tokens[i + 2]
    valid = lambda t: t.type in [MiniCLexer.Identifier, MiniCLexer.IntegerConstant]

    if valid(t1) and valid(t3):
        a = t1.text
        b = t3.text
        op = t2.text

        # جایگزینی نام‌ها اگر در نگاشت هستند
        if t1.type == MiniCLexer.Identifier and a in name_map:
            a = name_map[a]
        if t3.type == MiniCLexer.Identifier and b in name_map:
            b = name_map[b]

        if op == '+':
            return f"{a} - (-{b})", 3
        elif op == '-':
            return f"{a} + (-{b})", 3
        elif op == '*' and b == '2':
            return f"{a} << 1", 3
        elif op == '/' and b == '2':
            return f"{a} >> 1", 3
        elif op == '==':
            return f"!({a} != {b})", 3
        elif op == '&&':
            return f"!(!{a} || !{b})", 3
        elif op == '||':
            return f"!(!{a} && !{b})", 3

    return None, 1

def obfuscate_and_save(input_file, output_file, techniques):
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)
    tree = parser.program()

    visitor = ObfuscatorVisitor() if 'rename' in techniques else None
    name_map = {}

    if visitor:
        visitor.visit(tree)
        name_map = visitor.name_map

    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    tokens = token_stream.tokens
    no_space_tokens = {';', '(', ')', '{', '}', ','}
    dead_code_inserted = False

    with open(output_file, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.type == Token.EOF:
                break

            if 'expr' in techniques:
                replacement, skip = replace_expression_pattern(tokens, i, name_map)
                if replacement:
                    f.write(replacement + ' ')
                    i += skip
                    continue

            text = token.text

            if 'rename' in techniques and token.type == MiniCLexer.Identifier and text in name_map:
                text = name_map[text]

            f.write(text)


            if text == '{' and 'deadcode' in techniques and not dead_code_inserted:
                f.write('\n    ' + get_random_dead_code() + '\n')
                dead_code_inserted = True

            if text not in no_space_tokens:
                f.write(' ')

            if text == ';' and 'deadcode' in techniques and random.random() < 0.3:
                f.write('\n    ' + get_random_dead_code())

            if text == '}':
                dead_code_inserted = False

            i += 1

    print(f" فایل خروجی Obfuscated تولید شد: {output_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiniC Obfuscator Tool')
    parser.add_argument('--input', required=True, help='مسیر فایل ورودی')
    parser.add_argument('--output', required=True, help='مسیر فایل خروجی')
    parser.add_argument('--techniques', default='rename,deadcode,expr', help='تکنیک‌های Obfuscation به صورت comma-separated')

    args = parser.parse_args()
    
    selected_techniques = args.techniques.split(',')

    obfuscate_and_save(args.input, args.output, selected_techniques)

