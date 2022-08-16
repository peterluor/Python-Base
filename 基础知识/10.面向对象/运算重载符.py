# 构造函数__init__与析构函数__del__
# 用于创建对象与释放对象

class a:
    def __init__(self,value):
        self.value=value
        print('__init__:',value)
    def __del__(self):
        print('__del__:')
a1=a(1)

# 加减重载符__add__与__sub__
# 出现+ 和 — 才会调用
class b:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        self.v1=self.value+other
        return self.v1
    def __sub__(self,other):
        self.v2=self.value-other
        return self.v2
b1=b(5) # b1此时等于5
b2=b(7)
# print('add:',b1.__add__(3))
print('add:',b1+3)

# __str__
# 和str()功能一样

class MyClass: #自定义一个类
    def __init__(self, name , age): #定义该类的初始化函数
        self.name = name #将传入的参数值赋值给成员交量
        self.age = age
    def __str__(self): #用于将值转化为字符串形式，等同于 str(obj)
        return "name:"+self.name+";age:"+str(self.age)
# 此时会产生一个疑问,为什么要设置重载符,直接自己设置一个新方法不也可以实现
# 例如,__str__ 自己可以写一个str()方法，也可以实现字符串的转化
# 这就体现出了重载符的优点,除了一些特殊的运算,其余的 不需要自己刻意地调动,会自动的从头执行到尾部
mc=MyClass('zhang',17)
print(mc)

# 反向运算符,例如__add__,在Value+int不会出错,但是int+Value会报错,所以使用反向运算符