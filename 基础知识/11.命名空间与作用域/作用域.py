# 作用域就是一个 Python 程序可以直接访问命名空间的正文区域
# 常见的作用域有四种：
# L 最内层，包含局部变量
# E 包含了非全局也非局部的变量
# G 脚本的最外层，包含全局变量
# B 内置的变量以及函数

a=1                 # G作用域
def name():
    b=2
    c=3             # E作用域
    def age():
        d=3
        e=5         # L作用域
# 一个变量的检索顺序:L==>E==>G==>B
# 内置作用域是通过一个名为 builtin 的标准模块来实现的,可以查看当前脚本中定义了哪些变量
import builtins
print(dir(builtins))

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问

if True:
    a=1
else:
    pass
print(a)


