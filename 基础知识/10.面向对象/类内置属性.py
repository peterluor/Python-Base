
# __dict__:类的属性(返回一个字典,由类的数据属性组成)
# __doc__:类的文档字符串
# __name__:类名
# __bases__:类的父类构成元素(返回一个元组,由所有的父类构成)
# __module__:类的定义所在模块(类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于mymod)
# __class__:实例调用__class__属性时会指向该实例对应的类,然后继续调用以上类的属性
class human:
    def __init__(self,a,h,w):
        self.age=a
        self.hight=h
        self.weight=w
    def say(self):
        print('Age:{}\nHight:{}\nweight:{}'.format(self.age,self.hight,self.weight))
print('human_dict:',human.__dict__)
print('huamn_doc:',human.__doc__)
print('human_name:',human.__name__)
print('human_bases:',human.__bases__)
print('huaman_moudle:',human.__module__)
h1=human(1,2,3)
print('h1的类:',h1.__class__)
print('h1的类的名称:',h1.__class__.__name__)

