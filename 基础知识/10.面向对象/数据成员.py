# 又称为属性, 按照定义的位置,可以分为类属性和实例属性

# 类属性:定义在类中,但是在方法之外,通过类的名称或者实例名称进行访问,
# 可以在类的所有实例(包括各种方法)之间共享值,意思就是在类的北部和外部随便用
# 使用方法:类名称.类属性/ 实例名称.类属性，且可以直接当变量使用
class person:
    num=0
    age='18'
    hight='170'
    weight='60'
    def say(self,a,h,w):
        self.age1=int(person.age)+a #age1是实例属性吗？？是的话怎么访问？
        self.hight1=int(person.hight)+h
        self.weight1=int(person.weight)+w
        print('{},{},{}'.format(self.age1,self.hight1,self.weight1))
p1=person()
p1.say(1,2,3)
print(p1.age1)
p2=person()
print(person.age,p2.age) #类属性的调用方式有两种
#判断类属性是否可以共享
def share():
 if p1.num==p2.num:
     print('True')
 else:
     print('类属性不共享')

# 实例属性:在方法中定义的属性,只能作用于当前实例(方法)
# 但是在构造方法中创建的实例对象,可以在类的内部以及外部随便使用
# 只能通过实例名进行访问
class human:
    def __init__(self):
        self.a='17' #实例变量加不加self有啥区别
        self.h='170'
    def talk(self):
        self.w='60' #我如何在外部访问这个w
        print('a is {}\nh is {}'.format(self.a,self.h))
h1=human()
print(h1.a)
h1.talk()
h2=human()






