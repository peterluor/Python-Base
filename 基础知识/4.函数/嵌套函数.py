# 嵌套函数就是在一个函数中定义的函数
def new():
    def old():
        print('old')
    old()
new()