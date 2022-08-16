# 面向对象编程(OPP)就是对代码的一种封装
# 代码封装:即对实现功能的代码进行隐藏,仅留给用户使用的接口就像使用键盘鼠标,只会进行操作就行,不需要了解内部如何运行
# 面向对象编程将描述对象特征的数据以及代码块(函数)封装在一起,进而更好的描述真实的对象
# 类的继承: 子类是父类的延申,但是有具有子类独特的属性和行为,这个也被称为多态化
# 子类的所有实例是父类的实例,但父类的实例并不是字类的实例
# class ClassName(parameterlist)
# 当创建一个类时没有创建__init__()方法,则不用定义parameterlist参数

# 对一个人进行描述
# 表面特征:
# 肤色:黄色 体重:60kg 身高:170cm
# 行为描述:
# 会吃 会走 会说话 会睡觉

class human:
     bodycolor='yellow'
     weight='60kg'
     hight='170cm'
     # 会吃
     def eat(self):
          print('He can eat!')
     # 会走
     def walk(self):
          print('He can walk!')
     # 会说话
     def talk(self):
          print('He can talk!')
     # 会睡觉
     def sleep(self):
          print('He can sleep')
# 类的实例化
human_1=human() #因为__init__是空的,所以不需要任何参数就可以实例化
print('human.bodycolor:',human_1.bodycolor)
human_1.talk()
human.sleep(1)
# 调用类的方法时,可以先实例化后‘Class_Example_Name.FunctionName’或者‘ClassName.FunctionNmae(self,Arg1),slef也算参数，建议瞎写’

# 创建空类
class empty:
     pass

# 类(Class):有相同属性和方法的对象的组合,类就是一个模板,可以通过这个模板创建出无数的实例,例如human是一个类,通过human可以创建有不同特征的人。
# 方法:Class中定义的函数,方法中至少要有一个self参数
# 变量/属性:类中的所有变量就是属性,例如human中的bodycolor、weight、hight
# 类变量/类属性:在整个class中是通用的,定义在类中但是在方法(函数)之外,在所有的实例对象(包括各种方法)中都是共享使用的
# 数据成员:类变量或者实例变量中用于处理类及其实例对象的相关数据
# 方法重写:又称为方法覆盖,父类继承的方法不能满足子类的需求,则对方法进行改写
# 局部变量:定义在方法中的变量，只作用于当前实例的类
# 实例变量/实例属性:在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量,self.实例变量名
# 实例化:创建一个类的实例，类的具体对象
# 对象:通过类定义的数据结构实例,对象包括两个数据成员（类变量和实例变量）和方法，我们之前学习过的六种数据类型就是对象。因为类不能直接使用,所以需要
#    创建实例(对象)才可以使用,就相当于图纸和汽车,图纸就是类,汽车就是对象

