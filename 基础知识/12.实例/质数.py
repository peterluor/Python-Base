def zhishu(a):
    # 判断一个数是否为质数,不是则输出其银子
    counter=0   #计数器
    l=[]
    if a==0:
        print('0 既不是质数,也不是约数')
    elif a<0:
        print('只有自然数才有质数')
    else:
        for i in range(1,a+1):
            if a%i==0:
                counter=counter+1
                l.append(i)
            else:
                pass
    if counter<=2:
        print(a,'是质数')
    else:
        print(a,'不是质数')
        print(a,'的因子有:',l)
zhishu(6)
