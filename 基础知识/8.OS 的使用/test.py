# 使用 sys 模块之前，需使用 import 引入
import sys

try:
    x = int(input("请输入一个被除数："))
    print("30除以", x, "等于", 30 / x)
except:
    print(sys.exc_info())
    print("其他异常...")
