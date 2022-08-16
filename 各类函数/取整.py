import math
a,b=1.3,1.6
# 向下取整 int()
print('a向下取整为{},b向下取整为{}'.format(int(a),int(b)))
# 向上取整 ceil()
print('a向上取整为{},b向上取整为{}'.format(math.ceil(a),math.ceil(b)))  # 需要导入math模块
# 四舍五入 round()
print('a四舍五入为{},b四舍五入为{}'.format(round(a),round(b)))
# 分别取整数和小数部分 modf()
print(math.modf(a),math.modf(b))