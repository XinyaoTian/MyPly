# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:37'

import ply.lex as lex

import lexer


lexs = lex.lex(module=lexer)


with open('test_code.py', 'r') as f:
    data = f.read()


lexs.input(data)

for l in lexs:
    print(l)