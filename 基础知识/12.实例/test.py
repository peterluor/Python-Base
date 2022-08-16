def wei(a):
    s=str(a)
    l=[]
    for i in range(0,len(s)):
        b=int(s[i])
        l.append(b)
    return l
print(wei(123))