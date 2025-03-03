print('欢迎使用小呆自动求和器!小呆的第一段代码~')
num = int(input('请输入求和数字,不要输入小数!!!'))
print('正在计算...')

import datetime
timebefore = datetime.datetime.now()

a = -1
result = 0
for x in range(num + 1):
    result = x + result
    a = a + 1
    print(a)

timeafter = datetime.datetime.now()
deltatime = timeafter - timebefore

print('工作开始时间:',timebefore)
print('运算完成!结果为',result)
print('工作完成时间:',timeafter,'耗时',deltatime)