#Dictionary(字典)数据类型
print('-----------------------------------字典学习-----------------------------------')
#字典是一种映射类型，字典用{ }标识，它是一个无序的键(key):值(value) 的集合。
#键(key)必须使用不可变类型,且一个字典中键唯一。
#dict为字典构造函数,使用方法为如下。
#创建单键值字典 dict[键]=值
dict={} #创建一个空字典
dict[1]='python'
dict['python']=1
print(dict[1])
print(dict['python'])
#创建多键值字典-1 dict([(键值组1),(键值组2),(键值组3),……])
# g=dict([(1,'this'),(2,'is'),(3,'my'),(4,'python'),(5,'folder')])
# print(g)
# print(g.keys())
# print(g.values())
#创建多键值字典-2 a={键1:值1,键2:值2,键3:值3,……}
h={1:'this',2:'is',3:'my',4:'python',5:'folder'}
print(h)
print(h.keys()) #输出字典h的所有键
print(h.values()) #输出字典h的所有值
print(h[1]) #输出字典h中对应的键为 1 对应的值
#在某一些情况下,当指定的键的值不存在时,会报错,解决方法如下:
# 1.利用一个 if 语句进行判断输出
print('h.6:',h[6] if 6 in h else '查无此值')
# 2.给输出值一个默认值,存在则输出,不存在输出默认值
print('h.6:',h.get(6,'查无此值'))
for key,value in h.items(): #这里的h.items等同于keys+values
    # print('key:',key,'value',value)
    print('key:{} ====> value:{:12}'.format(key,value))
for key in h.keys():
    print('key:',key)
    print('key:{}'.format(key))
for value in h.values():
    print(value)