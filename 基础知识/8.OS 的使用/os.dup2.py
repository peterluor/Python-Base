# 复制一个文件描述符到另一个文件描述符
# os.dup2(fd,fd2) 将文件描述符fd复制到文件描述值fd2
# 没有返回值
# 等同于fd2=os.dup(fd)