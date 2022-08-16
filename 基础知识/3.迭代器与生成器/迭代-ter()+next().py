#迭代器只会从对象的第一个元素开始，一直到最后一个结束，只能向前不能后退
#常见的迭代有iter()和next(),二者经常是搭配使用的
#字符串、列表以及元组可以创建迭代器
list1=list(range(10))
print(list1)
it1=iter(list1)
for i in range(10):
 print(next(it1),end=' ')
print()
list2=list(range(2,20,2))
print(list2)
it2=iter(list2)
for j in it2:
    print(j,end=" ")