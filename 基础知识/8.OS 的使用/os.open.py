# 用于打开一个文件,并设置文件的各项属性
# os.open(file,flags,mode)
# file 是要打开的文件, flags是参数
# 返回值为新打开文件的文件描述符
    # os.O_RDONLY: 以只读的方式打开
    # os.O_WRONLY: 以只写的方式打开
    # os.O_RDWR : 以读写的方式打开
    # os.O_NONBLOCK: 打开时不阻塞
    # os.O_APPEND: 以追加的方式打开
    # os.O_CREAT: 创建并打开一个新文件
    # os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
    # os.O_EXCL: 如果指定的文件存在，返回错误
    # os.O_SHLOCK: 自动获取共享锁
    # os.O_EXLOCK: 自动获取独立锁
    # os.O_DIRECT: 消除或减少缓存效果
    # os.O_FSYNC : 同步写入
    # os.O_NOFOLLOW: 不追踪软链接
import os
fd=os.open(r'F:\Python\学习\基础知识\8.OS 的使用\test.txt',os.O_RDWR)
#写入字符串
os.write(fd,'\n这是我的Python文件夹'.encode())
os.close(fd)
