# 用于修改文件描述符的位置
# os.lseek(fd,pos,how)
# fd 文件描述符 pos 型对于固定参数how在文中的位置
# how是固定参数 SEEK_SET或者0 从文件开始位置计算pos
#             SEEK_CUR或者1 从当前位置开始计算pos
#             SEEK_END或者2 从文件结束位置计算pos
# os.lseek(fd,2,1) 文件描述符的位置为当前位置向后两个字符
# 没有任何返回值
# 文件描述符的位置相当于file中指针的位置
import os

fd = os.open(r'F:\Python\学习\基础知识\8.OS 的使用\test.txt',os.O_RDWR | os.O_CREAT)
os.write(fd,'This is my python floder'.encode()) # 一定要使用encode转换成固定格式
os.fsync(fd)
os.lseek(fd,2,0)
str2= os.read(fd,10)
print(str2)
