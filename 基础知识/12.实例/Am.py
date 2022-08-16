import int_len
def Am(a):
# 判断一个数是否为阿姆斯特丹数
    s = str(a)
    n=int_len.int_len(a)
    l=[]
    c=0
    for i in range(0,len(s)):
        b=int(s[i])
        l.append(b)
    for j in range(0,n):
        c=c+l[j]**n
    if a==c:
        return a
    else:
        pass
for i in range(1,1000):
    if isinstance(Am(i),int):
        print(Am(i))
    else:
        pass