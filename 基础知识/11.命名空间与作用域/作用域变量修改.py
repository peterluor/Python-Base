# global用于在内部作用域修改外部作用域的变量
# nonlocal用于修改嵌套作用域中的变量
a=1
b=1
def name():
    global a,b #使用global对要修改的变量进行声明
    # 在重新赋值之前变量值一直是全局变量定义的值
    print('修改前:',a,b)
    a=2
    b=3
    print('修改后:',a,b)
name()
def age():
    c=1
    def modify():
        nonlocal c
        print('修改前:',c)
        c=2
        print('修改后:',c)
    modify()
age()
