# with 表达式 as 变量
#     执行的语句块
# as可以被省略,先执行表达式,然后将表达式的执行结果赋值给变量,这个变量为全局通用的变量,不仅限于with中使用
# 相当于执行以下语句
# try:
#     变量=表达式
#     语句块
# finally:
#     exit()
import os
import sys

fd1 = os.open(r'F:\Python\test.txt', os.O_RDWR | os.O_CREAT)
os.write(fd1, str.encode('this is my python!'))  # 此处不把str转换为bytes,会显示报错
os.close(fd1)
# 当 os.write 出现错误时,剩下的语句 os.close(fd1) 不会被执行
try:
    fd2 = os.open(r'F:\Python\test.txt', os.O_RDWR | os.O_CREAT)
    os.write(fd2, str.encode('This is my folder'))
except:
    t = sys.exc_info()
    for i in range(0, len(t)):
        print('Error:{}'.format(i + 1), t[i])
finally:
    # noinspection PyUnboundLocalVariable
    os.close(fd2)
try:
    with os.open(r'F:\Python\test.txt',os.O_RDWR | os.O_CREAT) as fd3:
        os.write(fd3,str.encode('This is my python folder!'))
except:
    t = sys.exc_info()
    for i in range(0, len(t)):
        print('Error:{}'.format(i + 1), t[i])