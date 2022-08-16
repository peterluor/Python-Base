import os
path=input('请输入文件路径(结尾加上/)：')

# 获取该目录下所有文件，存入列表中
fileList=os.listdir(path)
def houzhui(s):
    a=s.rfind('.',0,len(s))
    for i in range(a,len(s)):
        for j in range(0,len(s)-a):
            s1[j]=s[i]
    return s1
def readhouzhui(l1):
    for i in range(0,len(l1)):
        houzhui(l1[i])
        print()
