# print函数,前面一直在用
# 将输出的值转换为字符串,可以使用str()和repr()函数
# str转出的格式用户易读,repr转出的格式解释器易读，str()更注重可读性，repr()更注重数据本身的信息
x,y=100,200
z1='x+y的值为'+str(x+y)
z2='x+y的值为'+repr(x+y)
print(z1)
print(z2)
hello1='hello\nworld!'
hello2=repr('hello\nworld') # repr可以输出转义字符
hello3=r'hello\nworld'
print(hello1)
print(hello2)
print(hello3)
# 实例:输出一个平方、立方表格
for i in range(1,11):
    print(i,i**2,i**3) # 左对齐
for i in range(1,11):
    print(str(i).rjust(2),str(i**2).rjust(3),str(i**3).rjust(4)) #右对齐
# 解释一下这里rjust后参数是2、3、4的原因
# range(1,11),最大的是10,平方最大的是三位数,所以平方是3,立方最大是4位数,所以立方是4
