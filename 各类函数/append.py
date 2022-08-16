# 在列表后面添加新的值
# list.append(object) object为添加的内容
l1=[]
for i in range(99):
    l1.append(i)
j=1
for j in range(len(l1)):
    if type(j/10)=='int':
         print(l1[j-1],'\n')
         j=j+1
    else:
        print(l1[j-1])
        j=j+1
