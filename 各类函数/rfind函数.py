#返回指定字符串最后出现的位置
# str.rfind(str1,begain,end)
# str 为查找的字符串, begin 为查找开始的位置, end 为查找结束的位置
s1=('this is my python folder')
s2='is'
print(s1.rfind(s2,0,len(s1)))
#写一个输出文件后缀的函数
def houzhui(s):
    a=s.rfind('.',0,len(s))
    for i in range(a,len(s)):
         print(s[i],end='')
houzhui('1.py')
print()
l=['1.py','2.txt','3.doc']
def readhouzhui(l1):
    for i in range(0,len(l1)):
        houzhui(l1[i])
        print()
readhouzhui(l)
