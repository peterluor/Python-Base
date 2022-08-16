# 用于从文件描述符 fd 中读取最多 n 个字节
# os.reaad(fd,n)
# fd是对应的文件描述符,n为读取的字符数
# 返回包含读取字节的字符串
import os
fd=os.open(r'F:\Python\test.txt',os.O_RDWR|os.O_CREAT|os.O_APPEND)
os.write(fd,'this is my folder'.encode())
os.lseek(fd,3,0)
str=os.read(fd,6)
print(str)
os.close(fd)