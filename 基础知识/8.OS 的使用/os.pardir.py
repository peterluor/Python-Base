# 获取当前目录的父目录
# os.pardir() 无参数
# 返回值为父目录的字符串
# 默认值为 “…”
import os
import keyword

path_now=os.getcwd()
# 父目录
path_parent=os.path.join(path_now,os.pardir)
# 输出
print('现在的目录为:',path_now)
print('父目录为:',os.path.abspath(path_parent))


