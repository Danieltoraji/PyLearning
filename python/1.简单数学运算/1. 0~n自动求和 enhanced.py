print('欢迎使用小呆自动求和器enhanced!优化了算法~')
num = int(input('请输入求和数字,不要输入小数!!!'))
print('正在计算...')

import datetime
timebefore = datetime.datetime.now()
print('工作开始时间:',timebefore)

number = range(num + 1)
first = number[0]
last = number[-1]

x = first + last
n = len(number)

result = int(x * n / 2)

timeafter = datetime.datetime.now()
deltatime = timeafter - timebefore

print('运算完成!结果为',result)
print('工作完成时间:',timeafter,'耗时',deltatime)
input('enter to exit')
