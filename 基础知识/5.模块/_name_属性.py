#一个模块被另一个程序第一次引入时，其主程序将运行。
#如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# if __name__=='__main__':
#     print('it runs')
# else:
#     print('other runs')
# a simple application
if __name__=='__main__':
    _name_属性()
else:
    pass