from dlexer import tokens

var_context = {}

precedence = (
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'REM', 'ADD'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('left', 'POW'),
)


# 处理逻辑控制相关
def get_conditions(params):
    params = list(params)
    result = params.pop()
    while len(params) >= 2:
        prev = result
        op = params.pop()
        comp = params.pop()
        result = {
            'and': lambda a, b: (a and b),
            'or': lambda a, b: (a or b),
        }[op](prev, comp)
    return result


def p_start(p):
    'start : function'


def p_function(p):
    '''
    function : function statement SPLIT
             | function line_statement
             | empty
    '''


def p_statement_none(p):
    'line_statement : SPLIT'


def p_statement_expr(p):
    'line_statement : expression SPLIT'
    p[0] = p[1]


# print语句
def p_statement_print(p):
    '''
    statement : PRINT LPAREN expr_list RPAREN
    '''
    print(''.join([str(i) for i in p[3]]))


# 赋值语句
def p_statement_assign(p):
    '''
    line_statement : ID ASSIGN expression SPLIT
                   | ID ASSIGN condition_list SPLIT
    '''
    p[0] = var_context[p[1]] = p[3]


# print功能扩展-多变量
def p_expression_list(p):
    '''
    expr_list : expression
              | expr_list COMMA expression
    '''
    if len(p) <= 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_condition_list(p):
    '''
    condition_list : expression
                   | condition_list AND expression
                   | condition_list OR expression
    '''

    if len(p) > 2:
        p[0] = get_conditions(params=p[1:])
    else:
        p[0] = p[1]


# 增加括号(控制语句)功能
def p_condition_parens(p):
    'condition_list : LPAREN condition_list RPAREN'
    p[0] = p[2]


# true
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True


# False
def p_expression_false(p):
    'expression : FALSE'
    p[0] = False


# 变量
def p_expression_var(p):
    'expression : ID'
    p[0] = var_context.get(p[1], 0)


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


# 增加括号(表达式)功能
def p_expression_parens(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# 出错功能
def p_error(p):
    print("Syntax error in input!", p)


def p_empty(p):
    'empty :'
