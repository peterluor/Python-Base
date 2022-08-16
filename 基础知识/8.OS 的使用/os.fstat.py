# 返回文件描述符的状态
# os.fstat(fd)   fd是文件描述符
# 返回值是一个包含文件描述符状态的元组,包含的内容结构如下:
# st_dev: 设备信息
# st_ino: 文件的i-node值
# st_mode: 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
# st_nlink: 硬连接数
# st_uid: 用户ID
# st_gid: 用户组 ID
# st_rdev: 设备 ID (如果指定文件)
# st_size: 文件大小，以byte为单位
# st_blksize: 系统 I/O 块大小
# st_blocks: 文件的是由多少个 512 byte 的块构成的
# st_atime: 文件最近的访问时间
# st_mtime: 文件最近的修改时间
# st_ctime: 文件状态信息的修改时间（不是文件内容的修改时间）
import os
fd=os.open(r'F:\Python\test.txt',os.O_RDWR)
#读取fd的状态元组
info=os.fstat(fd)
print('文件信息:',info)
print('设备信息:',info.st_dev)
print('文件的i—node值:',info.st_ino)
print('文件信息的掩码:',info.st_mode)
print('链接硬件数目:',info.st_nlink)
print('User UID:',info.st_uid)
print('Users UID:',info.st_gid)
print('size:',info.st_size)
print('文件最近的访问时间:',info.st_atime)
print('文件最近的修改时间:',info.st_mtime)

