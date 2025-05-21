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