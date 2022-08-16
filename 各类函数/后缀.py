# 该函数旨在输出指定文件夹下所有文件的后缀
import os
path=input('请输入路径\n')
l=os.listdir(path)
def houzhui(l):
    for i in range(0,len(l)):
        s=l[i]
        a=s.rfind('.')
        k=1 #计数器
        dict={}
        if a>0:
            for j in range(a,len(s)):
                if k<len(s)-a:
                    print(s[j],end='')
                    k=k+1
                elif k==len(s)-a:
                    print(s[j])
                else:
                    pass
        else:
            print('This is a folder')
    return
houzhui(l)