# open用于打开一个文件,并返回文件对象
# 打开一个文件后,一定要使用close()函数进行关闭
# file=open(file,mode,buffering,encoding,errors,newline,closefd,opener)\
#     file 文件路径 mode 打开模式 buffering 设置缓冲值 encoding 一般使用utf8
#     errors 报错级别 newline 区别换行符 closefd 传入的file参数类型 opener 自定义开启器
#
# 常见的mode
# t 文本模式  x 写模式,新建一个文件,文件存在就会报错 b 二进制模式
# + 打开文件进行更新(可读可写) r只读模式
# rb 二进制只读模式 rb+二进制打开文件进行读写 一般是非文本文件
# a打开一个文件用于追加,新的内容放在原有内容后

f=open(r'F:\Python\学习\基础知识\7.file的使用\test.txt','w') # f成为文件描述符
f.write('this is python folder')
f.close()
f=open(r'F:\Python\学习\基础知识\7.file的使用\test.txt','r')
str=f.read()
print(str)
f.close()
f=open(r'F:\Python\学习\基础知识\7.file的使用\test.txt','a')
str1='\n这是我的python文件夹'
f.write(str1)
f.close()



