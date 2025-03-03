import random

while True:
    answerint = random.randint(1111,9999)
    answer = str(answerint)
    ans1 = answer[0]
    ans2 = answer[1]
    ans3 = answer[2]
    ans4 = answer[3]
    answerlist = [ans1,ans2,ans3,ans4]
    if ans1 == ans2:
        pass
    elif ans1 == ans3:
        pass
    elif ans1 == ans4:
        pass
    elif ans2 == ans3:
        pass
    elif ans2 == ans4:
        pass
    elif ans3 == ans4:
        pass
    elif ans2 == '0':
        pass
    elif ans3 == '0':
        pass
    elif ans4 == '0':
        pass
    else:
        break

def guess(conjecture):
    res = []
    if int(conjecture) == answerint:
        res.append('666')
        return res
    else:
        conjecturestr = str(conjecture)
        conjecture1 = conjecturestr[0]
        conjecture2 = conjecturestr[1]
        conjecture3 = conjecturestr[2]
        conjecture4 = conjecturestr[3]
        if conjecture1 == ans1:
            res.insert(0,'A')
        elif answerlist.count(conjecture1) == 1:
            res.append('B')
        else:
            pass
        if conjecture2 == ans2:
            res.insert(0,'A')
        elif answerlist.count(conjecture2) == 1:
            res.append('B')
        else:
            pass
        if conjecture3 == ans3:
            res.insert(0,'A')
        elif answerlist.count(conjecture3) == 1:
            res.append('B')
        else:
            pass
        if conjecture4 == ans4:
            res.insert(0,'A')
        elif answerlist.count(conjecture4) == 1:
            res.append('B')
        else:
            pass
        return res

    


print('''欢迎来玩AB数游戏！
程序版本：1.1，程序作者：钉小呆Xiaodai. 。
游戏规则：系统生成一个各位数字互不相同且不为0的四位数。您来进行猜想。每猜到一个正确位置上的正确数字，显示一个A；猜到正确数字但不在正确位置者，显示一个B。
只允许输入四位正整数，以防程序报错。如果放弃请输入0000。
更新日志：1.优化了A,B的显示顺序；2.排除了含0的数。3.优化了启动逻辑。''')
times = 0
while True:
    times = times + 1
    print('这是您的第',times,'次猜想。')
    conj = str(input())
    if conj == '0000':
        print('太逊了！答案是：',answerint)
        input('按任意键退出')
        break
    else:
        pass
    result = guess(conj)
    if result.count('666') == 1:
        print('您赢了！答案是：',answerint,'您共猜了',times,'次。')
        input('按任意键退出')
        break
    else:
        print('您的猜想不正确，其结果是,',result)