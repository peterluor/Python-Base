#自己写完代码推出编辑器时,自己设置的变量以及方法就不能用了，所以就将这些文件打包,以便调用,这些文件称为模块
#模块是.py结尾的文件,可以被直接引用,以使用模块中的函数
#每个模块内部是独立的,所有符号可以全部使用,不用担心会给其余模块造成影响
#调用的模块要和主程序在同一目录下
#自己先编写一个判断偶数的程序test.py
import test
test.oushu(100)
test.fibo(20)
print()
from test import * #将test模块的所有导入到现在的空间内
#from a.b.c import d  #这是最常见的导入方法
oushu(100)
fibo(20)
print()






