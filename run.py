# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:37'

from ply import lex, yacc

import dlexer
import dparser
from dexecute import DyqExecute

lexs = lex.lex(module=dlexer)
parses = yacc.yacc(module=dparser)

with open('test_code.py', 'r') as f:
    data = f.read()

a = 3

if a == 1:
    lexs.input(data)
    for l in lexs:
        print(l)
elif a == 2:
    for x in parses.parse(data):
        print(x)
elif a == 3:
    for x in parses.parse(data):
        DyqExecute.resolve(x)