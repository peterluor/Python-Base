#必须参数:必须有的参数,不然会报错,调用时参数数量和定义时一样
#关键字参数,调用时可以用关键字参数就是函数传入的值,并且调用顺序和声明顺序可以不一致
def s(name,age,hight):
    print('Name:',name)
    print('Age:',age)
    print('Hight:',hight)
    return
s(hight='172',name='peter',age='21')
#默认参数,即在定义函数时对其中一个参数给一个确定的值,当使用此函数时,没有输入这个参数的值，则使用这个没默认参数
def default(a,b=5):
    c=a+b
    print('a+b=',c)
    return
default(a=3,b=7)
default(a=4)
#不定长参数
#在使用函数时,可能会输入比定义时更多的参数,这些参数成为不定长参数
#加了 * 的参数会以元组的形式导入
#加了 ** 的参数会以字典的形式导入
def long(a,*b):
    print(a)
    print(b)
    return
long(1,2,3,4,5)
def dictionary(a,**b):
    print(a)
    print(b)
    return
dictionary(1,b=2,c=3,d=4,e=5) # **调用以关键字的形式
#在声明函数时,* 可以单独出现,但是在调用时 * 后面的参数必须用关键字参数传入
def short(a,b,*,c):
    print('a+b+c=',a+b+c)
    return
short(1,2,c=4) #不 加关键字会报错

