class human:
    def __init__(self):
        self.a='17' #实例变量加不加self有啥区别
        self.h='170'
    def test(self):
        print(self.a,self.h)
h1=human()
h1.test()
a=1
print(a.__class__)