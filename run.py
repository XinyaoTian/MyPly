# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:37'

from ply import lex, yacc

import dlexer
import dparser


lexs = lex.lex(module=dlexer)
parses = yacc.yacc(module=dparser)

with open('test_code.py', 'r') as f:
    data = f.read()

a = 1

if a == 1:
    lexs.input(data)

    for l in lexs:
        print(l)
elif a == 2:
    result = parses.parse(data)
    if result:
        print(result)