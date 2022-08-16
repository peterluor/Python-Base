import os
import stat

# 设置路径标记为数字标记,多个标记可以用OR连接起来
# os.chflags(path,flags)
# path是文件名路径或目录路径,flags是标记值

# stat.UF_NODUMP 非转储文件
# stat.UF_IMMUTABLE 文件是只读
# stat.UF_APPEND 文件只能追加内容
# stat.UF_NOUNLINK 文件不可以删除
# stat.UF_OPAQUE 目录不透明，需要通过联合堆栈查看
# stat.SF_ARCHIVED 可存档文件(超级用户可设)
# stat.SF_IMMUTABLE 文件是只读的(超级用户可设)
# stat.SF_APPEND 文件只能追加内容(超级用户可设)
# stat.SF_NOUNLINK 文件不可删除(超级用户可设)
# stat.SF_SNAPSHOT 快照文件(超级用户可设)

# 没有返回值
path=r'F:\Python\test.txt'
flags=stat.UF_IMMUTABLE
os.chflags(path,flags)
