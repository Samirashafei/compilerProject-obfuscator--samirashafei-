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

def obfuscate_and_save(input_file, output_file, techniques):
    # مرحله اول: اگر تکنیک rename انتخاب شده، visitor را اعمال کن
    name_map = {}
    if 'rename' in techniques:
        input_stream_temp = FileStream(input_file, encoding='utf-8')
        lexer_temp = MiniCLexer(input_stream_temp)
        token_stream_temp = CommonTokenStream(lexer_temp)
        parser_temp = MiniCParser(token_stream_temp)
        tree = parser_temp.program()

        visitor = ObfuscatorVisitor()
        visitor.visit(tree)
        name_map = visitor.name_map

    # مرحله دوم: توکن‌ها را بخوان
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

            text = token.text

            # تکنیک rename
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

    print(f"✅ فایل خروجی Obfuscated تولید شد: {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MiniC Obfuscator Tool')
    parser.add_argument('--input', required=True, help='مسیر فایل ورودی')
    parser.add_argument('--output', required=True, help='مسیر فایل خروجی')
    parser.add_argument('--techniques', default='deadcode', help='تکنیک‌های Obfuscation به صورت comma-separated')

    args = parser.parse_args()
    selected_techniques = args.techniques.split(',')

    obfuscate_and_save(args.input, args.output, selected_techniques)
