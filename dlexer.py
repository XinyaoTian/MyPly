# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:38'

from re import escape
from ply.lex import TOKEN

# 状态控制
states = (
    ('string', 'inclusive'),
)

# 标识符
identify = ('NUMBER', 'ID', 'SPLIT', 'STRING')

# 保留字，TOKEN值为大写
reserved_list = ['true', 'false', 'print', 'and', 'or', 'if', 'else', 'for', 'in', 'range']
reserved = {s: s.upper() for s in reserved_list}

# 单字符的操作符 +-*/%><
operator_sg = {
    '+': 'ADD',
    '-': 'REM',
    '*': 'MUL',
    '/': 'DIV',
    '%': 'MOD',
    '<': 'LT',
    '>': 'GT',
    '(': 'LPAREN',
    ')': 'RPAREN',
    '=': 'ASSIGN',
    ',': 'COMMA',
    ':': 'COLON',
}

# 双字符的操作符
operator_se = {
    '>=': 'GE',
    '<=': 'LE',
    '==': 'EQ',
    '!=': 'NE',
    '**': 'POW',
}

"""
1. 配置tokens, 变量名必须为'tokens'
"""
tokens = list(identify) + list(reserved.values()) \
         + list(operator_sg.values()) + list(operator_se.values())

"""
2. 为token配置规则
"""


# 数字的规则(只支持int类型)
def t_NUMBER(t):
    r'(0|[1-9]\d*)'
    t.value = int(t.value)
    return t


# 保留字和变量一起配置(官网推荐的做法)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words, 如果是保留字，类型就是设置好的保留字类型，否则就是id类型
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


# 字符串起始位置
def t_STRING(t):
    r'["\']'
    t.lexer.begin('string')
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value


# 忽略所有以"'开头的字符, 也就是字符串的主体
def t_string_chars(t):
    r'[^"\']+'


# 字符串结束为止
def t_string_end(t):
    r'["\']'
    if t.lexer.str_marker == t.value:
        t.type = 'STRING'
        t.value = t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1]
        # 默认的状态是initial
        t.lexer.begin('INITIAL')
        return t


# 双字符的操作符要放在单字符操作符上面，优先匹配
operator_se_re = '(' + '|'.join(escape(x) for x in operator_se.keys()) + ')'


@TOKEN(operator_se_re)
def t_OPERATOR_SE(t):
    t.type = operator_se.get(t.value, 'SPECIAL')
    return t


# escape是将所有的字符自动转译成正则表达式能识别的字符
operator_sg_re = '[' + escape(''.join(operator_sg.keys())) + ']'


# 用装饰器将相应的正则表达式装载，原理是给__doc__赋值
@TOKEN(operator_sg_re)
def t_OPERATOR_SG(t):
    t.type = operator_sg.get(t.value, 'OPERATOR')
    return t


# 注释
def t_COMMENT(t):
    r'\#.*'


# 换行,同时也是语句的分隔符
def t_SPLIT(t):
    r'\n+|;+'
    t.lexer.lineno += len(t.value)
    return t


# 先忽略空格和tab符
t_ignore = ' \t'


# lex出错时的反应
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
