#数据类型转换
#数据类型的转换包括隐式数据转换和显式数据转换
print('------------------------------------------------------------')
print('------------------------隐式数据转换--------------------------')
#隐式数据转换中，不需要我们的干预,较低数据类型会自动向较高数据类型转换
num_int=1
num_float=1.23
num_new=num_int+num_float
print(type(num_int),type(num_float))
print(num_new,type(num_new))
print('------------------------------------------------------------')
print('------------------------显式数据转换--------------------------')
int1=123
str='2'
int2=int(str)
print(int2)
print('------------------------常见的显示转化函数--------------------')
print('-------------------------int()函数-------------------------')
#int函数是python的内置函数，作用就是把将一个字符串或数字转换为整型,具体的使用方法为int(x,base)
#若x为纯数字，则不能有base参数，否则报错;其作用为对入参x取整
int3=int(1.3)
print('int3=',int3)
#若x为str，则base可略可有。base存在时，视x为base类型数字，并将其转换为10进制数字。若x不符合base规则，则报错。
int4=int(str,3)
print('int4=',int4)
print('------------------------float()函数------------------------')
#float()函数用于将整数和字符串转换成浮点数 f=float(x), x为整数或者字符串
f1=float(1)
f2=float('123')
print(f1,f2)
#错误示范f3=float('this');print(f3)
print('-----------------------complex()函数-----------------------')
#complex(real,imag) real是复数的实部,imag是复数的虚部
#real--int,float,string imag--int,float
c1=complex(1,2)
c2=complex('1.1') #如果real是字符串,则不能有imag
c3=complex('1.1+2.2j')
print(c1,c2,c3)
