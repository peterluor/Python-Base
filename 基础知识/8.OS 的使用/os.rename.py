# 对文件或者目录进行重命名
# rename(s1,s2)
# 要修改的目录/文件名,修改后的目录/文件名
import  os
fd=os.open(r'F:\Python\学习\基础知识\8.OS 的使用\test.txt',os.O_RDWR|os.O_CREAT)
os.close(fd)
os.rename(r'F:\Python\学习\基础知识\8.OS 的使用\test.txt',r'F:\Python\学习\基础知识\8.OS 的使用\tes.txt')
