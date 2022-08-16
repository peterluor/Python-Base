# input函数不再多说
# open(filename,mode) 将会返回一个file对象,filename是访问文件的名称以及路径组成的字符串,mode是打开文件的模式
# 常见的模式如下图所示
# from PIL import Image
# img=Image.open(r'F:\Python\学习\基础知识\6.输入与输出\1.jpg')
# img.show()
f=open(r'F:\Python\学习\基础知识\6.输入与输出\project.txt','r+')
f.write('This is my Python\n 这是我的Python') # 用f.write命令写入
s1=f.write('\nthis\nis\nmy\npython') # 用f.write命令写入,但是返回的是写入的字符的个数,重复写会覆盖
print(s1)
s2=f.read()
s3=f.read(2) #f.read(size)表示从文件读取指针位置开始读 size 个字节,size省略则表示从从当前指针开始输出剩下的内容
f.close() # 记得关闭文件
# 如果写的不是字符串,就需要先转换成字符串再进行写入
f=open(r'F:\Python\学习\基础知识\6.输入与输出\test.txt','w') # 在“w”模式下,当前目录没有对应的文件,可以自动创建一个
l1=['this','is','my','Python','file']
s4=str(l1)
f.write(s4)
print(f.tell()) #返回文件对象当前所处的位置, 它是从文件开头到指针位置的字节数
f.close()
f=open(r'F:\Python\学习\基础知识\6.输入与输出\test.txt','r')
print(f.read(2)) # f.read(x)表示阅读前x个字节
print(f.tell())
f.close()
#f.seek(x,from_what) 改变文件读取指针当前的位置
# x表示移动的字符数,from_what有三种情况0、1、2,默认是0
# seek(x,0) 从文件的首行首字母向后移动x个字符
# seek(x,1) 从当前位置向后移动x个字符
# seek(-x,2) 从末尾向前移动x个字符
f=open(r'F:\Python\学习\基础知识\6.输入与输出\test.txt','rb+') #b表示二进制
s5=f.read()
print(s5)
f.seek(5,0) #移动文件读取指针移动到第四个位置
print(f.tell())
print(f.read(2)) #输出从当前指针开始的前两个字符

