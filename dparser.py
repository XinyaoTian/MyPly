from dlexer import tokens


def p_start(p):
    'start : function'


def p_function(p):
    '''
    function : function statement SPLIT
             | empty
    '''


# print语句
def p_statement_print(p):
    '''
    statement : PRINT LPAREN expression RPAREN
    '''
    print(p[3])


# true
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True


# False
def p_expression_false(p):
    'expression : FALSE'
    p[0] = False


# 标识符NUMBER
def p_expression_num(p):
    'expression : NUMBER'
    p[0] = int(p[1])


# 标识符STRING
def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]


# 二元操作符
def p_expression_two_operator(p):
    '''
    expression : expression ADD expression
               | expression REM expression
               | expression MUL expression
               | expression DIV expression
               | expression MOD expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression EQ expression
               | expression NE expression
               | expression POW expression
    '''
    p[0] = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
        '**': lambda x, y: x ** y,
    }[p[2]](p[1], p[3])


# 增加括号(语句)功能
def p_expression_parens(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# 出错功能
def p_error(p):
    print("Syntax error in input!", p)


def p_empty(p):
    'empty :'
