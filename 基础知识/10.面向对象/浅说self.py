# 为了说清楚 self 是个什么东西，你首选需要搞清实例与类之间的关系。
# 人就是一种类，人有名字，身高，体重等属性，不同人这些属性都是不一样的，除此之外，人还有很多方法（功能），例如，思考、跑步、睡觉等等。睡觉等等

class Person:
    def __init__(self, name):
        self.name = name

    def think(self):
        print("{} is thinking".format(self.name))
# 具体到每一个人，例如你自己，你身边的每一个具体的人，都是「人类」的实例对象，例如：

lisi = Person("lisi")
# 我构造了一个叫"lisi"的人，它是Person的实例对象，我们给Person定义了一个think方法，但是需要一个参数，我们可以把 lisi 这个实例对象传递过去。

Person.think(lisi)
# lisi is thinking
# 所以，这里的 self 其实就是函数 think 的一个普通参数而是，那为什么要叫self呢？其实这是约定俗成的，你叫其他名字也没关系，不过通常不这么做，就好比
# 我们平常交流都是用普通话，突然冒出一句洋文，别人不一定能听懂。

# 那为什么我们平常调用 think 方法的时候不是这样调用，而是直接用 「实例.方法」的形式调用呢？

Person.think
# <function Person.think at 0x110e4f510>

lisi.think
# <bound method Person.think of <__main__.Person object at 0x10f3a09b0>>
# 前者是一个在 Person 中的普通函数，后者是被绑定了的方法，该方法与当前实例对象进行了绑定，意味着 调用 lisi.think 时不再需要传递参数，因为已经
# 将lisi进行的绑定，调用的时候，python会自动把lisi作为参数传递过去。也就是说，调用的时候，会把当前对象自己传递过去。

lisi.think()
# lisi is thinking
