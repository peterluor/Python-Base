# 用于设置指定路径文件最后的修改时间和访问时间
# os.utime(path,times)
# path为文件路径,times是自己设置的参数
# times为None时,则修改访问和修改时间为当前时间,否则,则使用元组(atime,utime)分别修改访问时间和修改时间
import os
path=r'F:\Python\test.txt'
fd=os.open(path,os.O_RDWR|os.O_CREAT)
info=os.fstat(fd)
Num_1=info.st_mtime
Num_2=info.st_atime
print(Num_1,Num_2)
os.utime(path,(Num_1,Num_2))
