#这里给出了一种可能的包结构（在分层的文件系统中）
#sound/                          顶层包
      # __init__.py               初始化 sound 包
      # formats/                  文件格式转换子包
      #         __init__.py
      #         wavread.py
      #         wavwrite.py
      #         aiffread.py
      #         aiffwrite.py
      #         auread.py
      #         auwrite.py
      #         ...
      # effects/                  声音效果子包
      #         __init__.py
      #         echo.py
      #         surround.py
      #         reverse.py
      #         ...
      # filters/                  filters 子包
      #         __init__.py
      #         equalizer.py
      #         vocoder.py
      #         karaoke.py
      #         ...
# 目录只有包含一个叫做__init__.py的文件才会被认作是一个包.
# 最简单的情况,放一个空的__init__.py就可以了,当然这个文件中也可以包含一些初始化代码或者为(将在后面介绍的)__all__变量赋值.
# 使用代码引用子模块
# from sound.effects.echo import echofile
# echofile(a,b,……)
# 如果我们使用 from modname import* 命令时,python会把所有的子模块导入,但是由于windows无法区分大小写,所以 ECHO.py 导入后可能是echo.py
# 所以我们需要进行精确的索引
# 在 __init__.py 中定义一个列表变量 __all__,那么在使用 from modname import*命令时会将列表中的子模块导入
# __all__=['echo','surround','reverse']
# from sound.effect import*  #此时导入的是echo、surround、reverse三个子模块
# 但是这种会导致代码的可读性降低,不建议使用,多敲几下键盘就能解决