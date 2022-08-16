# 在创建一个类时,我们可以手动添加一个__init__方法,是一个特殊的方法,称为构造方法/构造函数
# 构造方法在创建对象时使用,每创建一个实例对象时,Python会自动调用
# 方法__init__可以自己加参数,但是至少需要一个参数self,且self必须放在第一位,仅有self的构造方法,称为类的默认构造方法
# 在进行类的实例化的过程中,会自动调用__init__()方法
# 在构造方法中 self 不需要手动传入参数
# self 代表的是类的实例，代表当前对象的地址
# self是一个指向实例本身的应用,用于访问类中的实例以及方法
class a:
    name='Baidu'
    url='www.baidu.com'
    def __init__(self,n,u):
        self.name1=n  #在构造方法中定义的实例变量,在其它方法中可以直接当变量使用
        self.url1=u
    def say(self):print('{}的地址是:{}'.format(self.name1,self.url1))
a1=a('Google','www.google.com') # __init__有两个参数,所以必须输入两个参数才能进行实例化
a2=a('Baiidu','www.baidu.com')
a.say(a1) # 此处的say是类a中的一个普通方法,在调用的时候需要一个参数self,我们把实例a1作为参数传过去
a1.say()    #此处的say是实例a1中的一个已经和a1绑定的方法,在调用的时候会自动把a1作为一个参数传过去
a.say(a2)