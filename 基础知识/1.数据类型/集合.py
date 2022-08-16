#set(集合)数据类型
print('-----------------------------------集合学习-----------------------------------')
#集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#基本功能是进行成员关系测试和删除重复元素。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
s= {'Google','Taobao','Runoob','Google','Facebook','Zhihu','Baidu'}
print(s) #集合每次的输出都会不一致,并且会自动去掉重复元素
# 成员测试
if 'Runoob' in s :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')
e=set('this') #set的使用格式为set(''),单括号中的内容为集合成员
f=set('is')
print(e,f)
print(e-f) #e和f的差集
print(e|f) #e和f的并集
print(e&f) #e和f的交集
print(e^f) #e和f中没有同时存在的元素
print('----------------------------------------------------------------------------')