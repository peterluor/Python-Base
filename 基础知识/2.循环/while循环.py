#break 语句用于跳出当前循环体
a=1
while a<=100: #循环语句后面要跟:
    if a%2==0:
        if a%3==0:
            print(a,'既可以整除2,也可以整除3')
        else:
            print(a,'只能整除2,但不能整除3')
    else:
        if a%3==0: #也可以写成 if(a%3==0):
            print(a, '不可以整除2,但可以整除3')
        else:
            print(a,'不能整除2,也不能整除3')
    a=a+1
# while循环也可以和else语句相结合
#   while 语句1
#       statement1
#    else
#       statement2
