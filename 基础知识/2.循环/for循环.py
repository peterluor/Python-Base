#for循环可以遍历任何可迭代对象，如一个列表或者一个字符串,for a in [范围值]
#break语句用于跳出当前循环体
#continue语句被用来跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
#range函数可以生成一个数列
#pass语句为键盘中断语句,只做占位使用,有的位置不写报错,写了也不行,就需要pass语句
lists1=[1,2,3,4,5,'this','is','my','python','folder']
for list1 in lists1:
    if list1!='my':
        print(list1,end=' ')
    else:
        break
print() #将两行隔开
for i in range(len(lists1)):
    print(i,lists1[i])
#输出一个可迭代序列的位置以及元素除了以上代码，还可以用函数enumerate
for i,j in enumerate(lists1):
    print(i,j)
print()
lists2=list(range(6)) #使用range函数创建一个列表
for list2 in lists2:
    print(list2,end=' ')
print()
lists3=range(1,9,2) #左闭右开区间
for list3 in lists3:
    print(list3,end=" ")
print()



