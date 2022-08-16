# 有时候语法并没有错误,但是会出现异常
# 使用 try except语句对异常进行捕捉
# while True: print('True')
# 会无限执行一个print 命令,但是当用户中止时, 会输出KeyboardInterrupt 命令
import sys

try:
    a = 1 / 2
    print(a)
    print(m) # 抛出NameError异常
    b = 1 / 0
    print(b)
    c = 2 / 1
    print(c)
except NameError:
    print("Ops!!")  # 捕获到异常
except ZeroDivisionError:
    print("Wrong math!!")
except:
    print("Error")
else:
    print("No error! yeah!")
finally:      # 是否异常都执行该代码块
    print("Successfully!")
# 提取异常
try:
    while True:
        print("It's True!")
except:
    print("Unexpected error:",sys.exc_info())

# try/except的执行顺序
# 1.先执行try下的子句,没有出现异常,继续执行try语句,忽略except中的语句
# 2.当执行try过程中出现异常时,剩下的语句将不被执行。异常和except后的语句一致时,则执行except后的语句
# 3.如果异常和任何except后的语句相符合,则返回try
# 4.一个try可以包含多个except语句,最多执行一个,一个except后面可以跟多个异常,多个异常以元组的形式组合.
# 5.except (KeyboardInterrupt,KeyError,LookupError)
# 6.except后面也可以是空语句,然后可以使用sys.exc_info()语句对异常信息进行捕获,也可以空置直接执行except后的语句
# 7.sys.exc_info()提取的异常信息是一个长度为3的元组,分别为错误类型、错误举例以及traceback语句
# 8.要查看 traceback 对象包含的内容，需要先引进 traceback 模块，然后调用 traceback 模块中的 print_tb 方法，并将 sys.exc_info()
#   输出的 traceback 对象作为参数参入 traceback.print_tb(sys.exc_info()[2])
# 9.try except 后面可以跟一个else 语句,当没有异常发生时,可以执行else中的语句
