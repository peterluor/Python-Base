# # 使用 raise 语句抛出一个指定的异常
# raise Exception()
# Exctption 时raise唯一的参数,参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类(也就是 Exception 的子类)
# import sys
#
# try:
#     x = 10
#     if x > 5:
#         raise Exception('x不能大于5,x的值为:{}'.format(x))
# except:
#     print(sys.exc_info())
try:
        raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise