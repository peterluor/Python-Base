# class sonclassname(daaclassname):

class person:
    age='18'
    weight='60'
    hight='170'
    def new(self,a,w,h):
        self.age1=int(person.age)+a  #self.变量名 是一个实例属性,在定义类的的所有方法中是通用的
        self.weight1=int(person.weight)+w
        self.hight1=int(person.hight)+h
    def soeak(self):
        print('年龄为:{}\n体重为:{}\n身高为:{}'.format(self.age1,self.weight1,self.hight1))
class human(person):
    color='yellow'
    def new_1(self,a,w,h,c):
        person.new(self,a,w,h) #调用父类的方法进行继承
        self.color=c
    def speak(self):
        print('年龄为:{}\n体重为:{}\n身高为:{}\n肤色为:{}'.format(self.age1,self.weight1,self.hight1,self.color))
p1=person()
h1=human()
h1.new_1(1,2,3,4)
h1.speak()


# 多继承
# class sonclassname(dadclassname1,dadclassname2)
class human_1:
    def new_2(self,c):
        self.color=c
class student(person,human_1):
    def new_3(self,a,w,h,c):
        person.new(self,a,w,h)
        human_1.new_2(self,c)
    def speak(self):
        human.speak(self)
s1=student()
s1.new_3(1,2,3,4)
s1.speak()

#重写
# 在继承父类的过程中,对父类的方法不满意,可以在子类中重新编写方法
