# try-finally 语句无论是否发生异常都将执行最后的代码
import sys

try:
    runoob()
except KeyboardInterrupt:
    print('None')
except:
    t = sys.exc_info()
    for i in range(0, len(t)):
        print('Error{}:'.format(i + 1), t[i])
else:
    pass
finally:
    print('最终都要输出的内容')
