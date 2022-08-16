# 用于检验文件路径的权限
# os.access(path,mode)
# path是文件名路径或文件路径, mode是检验参数, 常见的有
# os.F_OK    检验路径是否存在
# os.R_OK    检验路径是否可读
# os.W_OK    检验路径是否可写
# os.X_OK    检验路径是否可以执行
# 存在返回true,不存在返回False
import os
path=r'F:\Python\学习\基础知识\8.OS 的使用'
print(os.access(path,os.F_OK))
print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))
