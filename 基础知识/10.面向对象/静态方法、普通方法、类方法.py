# 静态方法 用@staticmethod修饰且不带self参数的方法称为静态方法,调用时可以直接使用类名调用
# 类方法 用@classmethod方法修饰且带一个cls参数,可以直接使用类名调用
# 普通方法 默认带self参数,只能使用对象名调用
import builtins

class classname:
    def method_1(self):
        print('oridinary method')
    @staticmethod
    def method_2():
        print('jingtai method')
    @classmethod
    def method_3(cls):
        print('CLass method')
c=classname()
c.method_1()
classname.method_2()
classname.method_3()
dir(builtins)