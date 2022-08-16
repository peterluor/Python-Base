# 字符串.rjust(width,[fillchar])
# width 填充的宽度, fillchar 填充的字符,默认是空格
# 返回一个右对齐,并使用fillchar填充至长度width的新字符串
# 如果width小于字符串长度则返回原字符串
# 类似的有ljust、cjust
s1='this is my python folder!'
s2=s1.rjust(27)
s3=s1.zfill(27) #zfill函数相当于rjust中的fillchar是0
print(len(s1))
print(s1)
print(s2)
print(s3)

