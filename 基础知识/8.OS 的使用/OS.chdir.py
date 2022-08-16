#用于改变文件的工作路径到现在的路径
# os.chdir(path) path为切换到的新的路径
# 没有返回值
import os
# 切换工作路径到 F:\Python
path=r'F:\Python'
os.chdir(path)
# 读取当前的工作路径
print(os.getcwd()) # getcwd()函数是一个读取工作路径的函数,返回当前的工作路径
