# string数据
s='string'
# bytes数据
b=b'bytes'
# str ==> bytes
b1=bytes(s,encoding='utf8')
b2=str.encode(s)
print('convert byte:\n',b1,'\n',b2)
# bytes ==> string
s1=str(b,encoding='utf-8')
s2=bytes.decode(b)
print('convert string:\n',s1,'\n',s2)

