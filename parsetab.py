
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER ID SPLIT STRING TRUE FALSE PRINT ADD REM MUL DIV MOD LT GT LPAREN RPAREN ASSIGN GE LE EQ NE POWstart : function\n    function : function statement SPLIT\n             | empty\n    \n    statement : PRINT LPAREN expression RPAREN\n    expression : TRUEexpression : FALSEexpression : NUMBERexpression : STRING\n    expression : expression ADD expression\n               | expression REM expression\n               | expression MUL expression\n               | expression DIV expression\n               | expression MOD expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression EQ expression\n               | expression NE expression\n               | expression POW expression\n    expression : LPAREN expression RPARENempty :'
    
_lr_action_items = {'PRINT':([0,2,3,6,],[-22,5,-3,-2,]),'$end':([0,1,2,3,6,],[-22,0,-1,-3,-2,]),'SPLIT':([4,15,],[6,-4,]),'LPAREN':([5,7,8,16,17,18,19,20,21,22,23,24,25,26,27,],[7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'TRUE':([7,8,16,17,18,19,20,21,22,23,24,25,26,27,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'FALSE':([7,8,16,17,18,19,20,21,22,23,24,25,26,27,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'NUMBER':([7,8,16,17,18,19,20,21,22,23,24,25,26,27,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'STRING':([7,8,16,17,18,19,20,21,22,23,24,25,26,27,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'RPAREN':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[15,-5,-6,-7,-8,28,-21,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,]),'ADD':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[16,-5,-6,-7,-8,16,-21,16,16,16,16,16,16,16,16,16,16,16,16,]),'REM':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[17,-5,-6,-7,-8,17,-21,17,17,17,17,17,17,17,17,17,17,17,17,]),'MUL':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[18,-5,-6,-7,-8,18,-21,18,18,18,18,18,18,18,18,18,18,18,18,]),'DIV':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[19,-5,-6,-7,-8,19,-21,19,19,19,19,19,19,19,19,19,19,19,19,]),'MOD':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[20,-5,-6,-7,-8,20,-21,20,20,20,20,20,20,20,20,20,20,20,20,]),'GT':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[21,-5,-6,-7,-8,21,-21,21,21,21,21,21,21,21,21,21,21,21,21,]),'LT':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[22,-5,-6,-7,-8,22,-21,22,22,22,22,22,22,22,22,22,22,22,22,]),'GE':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[23,-5,-6,-7,-8,23,-21,23,23,23,23,23,23,23,23,23,23,23,23,]),'LE':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[24,-5,-6,-7,-8,24,-21,24,24,24,24,24,24,24,24,24,24,24,24,]),'EQ':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[25,-5,-6,-7,-8,25,-21,25,25,25,25,25,25,25,25,25,25,25,25,]),'NE':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[26,-5,-6,-7,-8,26,-21,26,26,26,26,26,26,26,26,26,26,26,26,]),'POW':([9,10,11,12,13,14,28,29,30,31,32,33,34,35,36,37,38,39,40,],[27,-5,-6,-7,-8,27,-21,27,27,27,27,27,27,27,27,27,27,27,27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'function':([0,],[2,]),'empty':([0,],[3,]),'statement':([2,],[4,]),'expression':([7,8,16,17,18,19,20,21,22,23,24,25,26,27,],[9,14,29,30,31,32,33,34,35,36,37,38,39,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> function','start',1,'p_start','dparser.py',7),
  ('function -> function statement SPLIT','function',3,'p_function','dparser.py',12),
  ('function -> empty','function',1,'p_function','dparser.py',13),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','dparser.py',20),
  ('expression -> TRUE','expression',1,'p_expression_true','dparser.py',27),
  ('expression -> FALSE','expression',1,'p_expression_false','dparser.py',33),
  ('expression -> NUMBER','expression',1,'p_expression_num','dparser.py',39),
  ('expression -> STRING','expression',1,'p_expression_string','dparser.py',45),
  ('expression -> expression ADD expression','expression',3,'p_expression_two_operator','dparser.py',52),
  ('expression -> expression REM expression','expression',3,'p_expression_two_operator','dparser.py',53),
  ('expression -> expression MUL expression','expression',3,'p_expression_two_operator','dparser.py',54),
  ('expression -> expression DIV expression','expression',3,'p_expression_two_operator','dparser.py',55),
  ('expression -> expression MOD expression','expression',3,'p_expression_two_operator','dparser.py',56),
  ('expression -> expression GT expression','expression',3,'p_expression_two_operator','dparser.py',57),
  ('expression -> expression LT expression','expression',3,'p_expression_two_operator','dparser.py',58),
  ('expression -> expression GE expression','expression',3,'p_expression_two_operator','dparser.py',59),
  ('expression -> expression LE expression','expression',3,'p_expression_two_operator','dparser.py',60),
  ('expression -> expression EQ expression','expression',3,'p_expression_two_operator','dparser.py',61),
  ('expression -> expression NE expression','expression',3,'p_expression_two_operator','dparser.py',62),
  ('expression -> expression POW expression','expression',3,'p_expression_two_operator','dparser.py',63),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parens','dparser.py',83),
  ('empty -> <empty>','empty',0,'p_empty','dparser.py',93),
]
