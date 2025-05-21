grammar MiniC;

program: (structDefinition | functionDefinition | declaration)* EOF;

// === تعریف struct ===
structDefinition
    : 'struct' Identifier '{' declaration* '}' ';';

// === تعریف تابع ===
functionDefinition
    : typeSpecifier pointerSpecifier? Identifier '(' parameterList? ')' compoundStatement;

// === پارامترهای تابع ===
parameterList: parameter (',' parameter)*;
parameter: typeSpecifier pointerSpecifier? Identifier;

// === تعریف متغیر ===
declaration: typeSpecifier pointerSpecifier? initDeclaratorList ';';

initDeclaratorList: initDeclarator (',' initDeclarator)*;
initDeclarator: Identifier ('=' expression)?;

// === انواع داده ===
typeSpecifier
    : 'int' | 'char' | 'bool' | 'struct' Identifier;

pointerSpecifier
    : '*'*;

// === بدنه کد ===
compoundStatement: '{' (statement | declaration)* '}';

statement
    : expressionStatement
    | compoundStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    | ioStatement;

expressionStatement: expression? ';';

selectionStatement
    : 'if' '(' expression ')' statement ('else' statement)?;

iterationStatement
    : 'while' '(' expression ')' statement
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement;

jumpStatement: 'return' expression? ';';

ioStatement
    : 'printf' '(' STRING_LITERAL (',' expression)* ')' ';'
    | 'scanf' '(' STRING_LITERAL (',' '&'? Identifier)* ')' ';';

// === عبارات ===
expression
    : assignmentExpression;

assignmentExpression
    : logicalOrExpression ('=' assignmentExpression)?;

logicalOrExpression
    : logicalAndExpression ('||' logicalAndExpression)*;

logicalAndExpression
    : equalityExpression ('&&' equalityExpression)*;

equalityExpression
    : relationalExpression (('==' | '!=') relationalExpression)*;

relationalExpression
    : additiveExpression (('<' | '<=' | '>' | '>=') additiveExpression)*;

additiveExpression
    : multiplicativeExpression (('+' | '-') multiplicativeExpression)*;

multiplicativeExpression
    : unaryExpression (('*' | '/' | '%') unaryExpression)*;

unaryExpression
    : ('+' | '-' | '!' | '&' | '*')? postfixExpression;

// === استفاده از تابع، اشاره‌گر یا عضوی از struct ===
//امتیازی
postfixExpression
    : primaryExpression ('.' Identifier | '->' Identifier | '(' argumentList? ')')*;

primaryExpression
    : Identifier
    | Constant
    | '(' expression ')';

argumentList: expression (',' expression)*;

// === ثابت‌ها ===
Constant
    : IntegerConstant
    | CharacterConstant
    | BooleanConstant;

IntegerConstant: [0-9]+;
CharacterConstant: '\'' . '\'';
BooleanConstant: 'true' | 'false';

// === توکن‌ها ===
Identifier: [a-zA-Z_][a-zA-Z_0-9]*;
STRING_LITERAL: '"' (~["\\] | '\\' .)* '"';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;
