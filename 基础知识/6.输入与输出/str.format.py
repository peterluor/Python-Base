import math
# 字符串.format也用于输出
# 这个字符串是一个有特殊格式的字符串
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换，括号外的保持不变
print('{} and {}'.format('google','baidu')) #当括号为空时,format中的参数会依次替换括号
# str.format可以用于赋值
a='{} and {}'.format('google','baidu')
print(a)
print('{0} and {1}'.format('sogou','yaho'))
print('{1} and {0}'.format('sogou','yaho')) #当括号中为数字时，数字表示format中的位置,会输出对应位置的参数
print('Name:{name}\nWeight:{weight}'.format(weight='60',name='peterluor')) # 当括号中为关键字时,会输出该关键字对应的参数
# 常见的设置索引的方式
site = {"name":"百度","url":"www.baidu.com"} # 使用字典设置索引
print("网站名:{name} 地址:{url}".format(**site)) # “**”是必不可少的
list1=['百度','www.baidu.com'] # 使用列表
print('网站名:{0[0]} 地址:{0[1]}'.format(list1))  # 0是必不可少的
tuple1=('百度','www.baidu.com') # 使用元组
print('网站名:{0} 地址:{1}'.format(*tuple1)) # "*"是必不可少的
#'{a: }'.format(str) 冒号后跟不同的数字表示不同的含义
b=('{0:8} ---   {1:8}'.format('google','baidu')) # :整数,表示该域的最小长度
print(b)
# 后面跟不同的字符有不同的含义,后跟 .2f 表示保留两位小数，+.2f表示保留两位小数且保留“+”
# 更多详见https://www.runoob.com/python/att-string-format.html#:~:text=value%20%E4%B8%BA%3A%206-,%E6%95%B0%E5%AD%97%E6%A0%BC%E5%BC%8F%E5%8C%96,-%E4%B8%8B%E8%A1%A8%E5%B1%95%E7%A4%BA%E4%BA%86
c='常量的近似值为:%5.2f'%math.pi # %也是一个数字格式转换符, % 等同于format中的 {} ,5 等同于format中的 :
print(c)
