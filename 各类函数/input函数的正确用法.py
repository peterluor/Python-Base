# #input('提示语句')
# input默认输入的是字符串形式
a=input('please input a int\n')
a=int(a)
if a%2==0:
    print('您输入的',a,'是一个偶数')
else:
    print('您输入的',a,'是一个奇数')