from dlexer import tokens

from dexecute import DyqExecute

exelist = []

precedence = (
    # ('nonassoc', 'IFX', 'SPLIT'),
    # ('left', 'CONDLIST'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'REM', 'ADD'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('left', 'POW'),
)


def p_start(p):
    'start : function'
    p[0] = exelist


def p_function(p):
    '''
    function : function statement SPLIT
             | function line_statement
             | empty
    '''
    if len(p) > 2:
        exelist.append(p[2])
        p[0] = p[2]


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
    p[0] = DyqExecute(action='print', params=p[3])


# 生成一个list对象记录着每个迭代的次数
def p_range(p):
    'range : RANGE LPAREN expr_list RPAREN'
    print('is range', p)
    p[0] = list(range(p[3][0], p[3][1]))
    print('is range', p[0])


def p_statement_for(p):
    'line_statement : FOR ID IN range COLON statement SPLIT'
    p[0] = DyqExecute(action='loop', params=[p[2], p[4], p[6]])


def p_statement_cond_postfix_else(p):
    'line_statement : statement IF condition_list ELSE statement SPLIT'
    p[0] = DyqExecute(action='condition', params=[p[3], p[1], p[5]])


def p_ifassign(p):
    'if_assign : ID ASSIGN expression'
    p[0] = [p[1], p[3]]


def p_statement_cond_postfix_assign(p):
    'line_statement : if_assign IF condition_list ELSE expression SPLIT'
    p[0] = DyqExecute(action='assign', params=[
        p[1][0], DyqExecute(action='condition', params=[p[3], p[1][1], p[5]])
    ])


# IF语句(少两个优先级的判定)
def p_statement_cond(p):
    '''
    line_statement : IF condition_list COLON statement SPLIT
                   | IF condition_list COLON SPLIT statement SPLIT
    '''
    # 分为上面两种情况，一个stmt的位置在4,一个在5(0开始计数)
    if len(p) < 7:
        p[0] = DyqExecute(action='condition', params=[p[2], p[4]])
    else:
        p[0] = DyqExecute(action='condition', params=[p[2], p[5]])


# 赋值语句
def p_statement_assign(p):
    '''
    line_statement : ID ASSIGN expression SPLIT
                   | ID ASSIGN condition_list SPLIT
    '''
    p[0] = DyqExecute(action='assign', params=[p[1], p[3]])


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


# 逻辑控制语句(少一个优先级)
def p_condition_list(p):
    '''
    condition_list : expression
                   | condition_list AND expression
                   | condition_list OR expression
    '''

    if len(p) > 2:
        p[0] = DyqExecute(action='logop', params=p[1:])
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
    p[0] = DyqExecute(action='get', params=[p[1]])


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
    p[0] = DyqExecute(action='binop', params=p[1:])


# 增加括号(表达式)功能
def p_expression_parens(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# 出错功能
def p_error(p):
    print("Syntax error in input!", p)


def p_empty(p):
    'empty :'


def debug(*params):
    print("[DBG] %s" % (' : '.join(str(x) for x in params),))