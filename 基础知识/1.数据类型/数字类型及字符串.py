# 这是数字类型以及字符串的学习文件
# 整数型(int)
a=1
# 浮点型(float)
b=1.23
# 布尔型(bool)
# 复数型(complex)
c=1+2j  #注意这里只能是j
print(a,b)
print(c.real)
print(c.imag)
#Python 中单引号 ' 和双引号 " 使用完全相同。
a1="hello world"
a2='hello world'
print(a1)
print(a2)
# 使用双三引号(''' 或 """)可以指定一个多行字符串。
a3='''你是风
你是光
你是唯一的神话
'''
print(a3)
# \反斜杠表示转义,和特定字母组合会产生不同的意思,r表示raw string,可以让反斜杠不转义，输出反斜杠
a4='hello\nworld'
a5=r'hello\nworld'
print(a4)
print(a5)
# 字符串可以用 + 运算符连接在一起，用 * 运算符表示重复次数
s1='hello,'
s2='world!'
s3=s1+s2
s4=s1*2
print('s1+s2=',s3)
print('s1*2=',s4)
# Python 中的字符串有两种索引方式，从左往右以0,1,2,3……开始，从右往左以-1,-2,-3……开始
# 索引格式为s[***]
# 在一个字符串中空格的长度为1
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长],例如[1:4]表示从2到4的所有字符，[1:6:2]表示从2到6且每隔两个的所有字符
s='this is string!'
print(s[6])#输出字符串从左到右的第七个字符
print(s[0:7:2])#输出字符串从左到右，1到7且每隔两个长度的所有字符，1，3，5，7
print(s[-2])#食醋胡字符串从右到左第2个字符
print(s[2:])#输出字符串从左到右第三个字符后的所有字符
#用户输入 input 按下enter键会自己退出
input('please enter')
# Python 可以在同一行中使用多条语句，语句之间使用分号;分割
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=" "/end=' '
print(a);print(b);print(c.real);print(c.imag)
print(a,end=' ')
print(b,end=' ' )
print(c.real,end=' ' )
print(c.imag)
print(a,b,c.real,c.imag)








