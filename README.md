
### 目录
1. 项目介绍
2. 项目结构介绍
3. 使用方法
4. 词法分析介绍
5. 语法分析介绍

#### 一. 项目介绍
python版本为3.6。

使用库为ply。

模仿python语法完成一小部分功能，例如注释，二元运算符，逻辑运算符，print语句，for语句，if语句，if-else语句，基本数据类型有int，string，boolean，变量。

#### 二. 项目结构介绍
1. dlexer.py 实现了词法分析
2. dparser.py 实现了语法分析
3. dexecute.py 实现了执行语法的功能
4. test_code.py 要进行测试的代码
5. run.py 执行文件，从test_code中读入代码，可调整choice变量，执行1-3的功能

#### 三. 使用方式
1. 首先创建一个文件用于写测试代码(自带的测试文件为test_code.py)
2. run.py中会加载1中创建的文件(默认加载为test_code.py)
3. 更改choice变量的值，可更改值有1(词法),2(语法),3(执行)(默认choice的值为3)

#### 四. 词法分析
1. 标识符
    1. NUMBER 整数类型
    2. ID 变量
    3. STRING 字符串类型
    4. SPLIT 语句间的分隔符
2. 保留字
    1. TRUE/FALSE bool类型
    2. print/range 常用的函数
    3. and/or 逻辑运算符
    4. if/else 条件
    5. for/in 循环
3. 单字符操作符
    1. ADD/REM/MUL/DIV/% 加减乘除除余
    2. LT/GT/ASSIGN 大于小于赋值
    3. LPAREN/RPAREN 左右括号
    4. COMMA/COLON 逗号冒号
4. 双字符操作符
    1. GE/LE 大于等于/小于等于
    2. EQ/NE 等于/不等于
    3. ** 乘方
5. 注释

    \# 由井号开头的一行将被忽略
    
#### 五. 语法分析


```python
Rule 0     S' -> entry

Rule 1     entry -> start

Rule 2     start -> start stmt_print SPLIT
Rule 3     start -> start stmt
Rule 4     start -> empty

Rule 5     stmt -> SPLIT
Rule 6     stmt -> expression SPLIT
# print
Rule 7     stmt_print -> PRINT LPAREN expr_list RPAREN
# for
Rule 8     range -> RANGE LPAREN expr_list RPAREN
Rule 9     stmt -> FOR ID IN range COLON stmt_print SPLIT
# if-else
Rule 10    stmt -> stmt_print IF condition_list ELSE stmt_print SPLIT
Rule 11    if_assign -> ID ASSIGN expression
Rule 12    stmt -> if_assign IF condition_list ELSE expression SPLIT
Rule 13    stmt -> IF condition_list COLON stmt_print SPLIT
Rule 14    stmt -> IF condition_list COLON SPLIT stmt_print SPLIT
# 赋值
Rule 15    stmt -> ID ASSIGN expression SPLIT
Rule 16    stmt -> ID ASSIGN condition_list SPLIT
# 一行多个表达式
Rule 17    expr_list -> expression
Rule 18    expr_list -> expr_list COMMA expression
# 逻辑控制
Rule 19    condition_list -> expression
Rule 20    condition_list -> condition_list AND expression
Rule 21    condition_list -> condition_list OR expression
Rule 22    condition_list -> LPAREN condition_list RPAREN
# 标识符
Rule 23    expression -> TRUE
Rule 24    expression -> FALSE
Rule 25    expression -> ID
Rule 26    expression -> NUMBER
Rule 27    expression -> STRING
# 二元运算
Rule 28    expression -> expression ADD expression
Rule 29    expression -> expression REM expression
Rule 30    expression -> expression MUL expression
Rule 31    expression -> expression DIV expression
Rule 32    expression -> expression MOD expression
Rule 33    expression -> expression GT expression
Rule 34    expression -> expression LT expression
Rule 35    expression -> expression GE expression
Rule 36    expression -> expression LE expression
Rule 37    expression -> expression EQ expression
Rule 38    expression -> expression NE expression
Rule 39    expression -> expression POW expression
Rule 40    expression -> LPAREN expression RPAREN
Rule 41    empty -> <empty>
```
