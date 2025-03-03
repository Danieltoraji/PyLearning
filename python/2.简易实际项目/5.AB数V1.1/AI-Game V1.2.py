import random

def generate_unique_number():
    while True:
        answerint = random.randint(1111, 9999)
        answer = str(answerint)
        if len(set(answer)) == 4 and '0' not in answer:
            return answerint, answer

def guess(conjecture, answerint, answerlist):
    res = []
    if int(conjecture) == answerint:
        res.append('666')
        return res

    for i in range(4):
        if conjecture[i] == answerlist[i]:
            res.insert(0, 'A')
        elif conjecture[i] in answerlist:
            res.append('B')
    
    return res

def main():
    print('''欢迎来玩AB数游戏！
    程序版本：1.1，程序作者：钉小呆Xiaodai. 。
    游戏规则：系统生成一个各位数字互不相同且不为0的四位数。您来进行猜想。每猜到一个正确位置上的正确数字，显示一个A；猜到正确数字但不在正确位置者，显示一个B。
    只允许输入四位正整数，以防程序报错。如果放弃请输入0000。
    更新日志：1.优化了A,B的显示顺序；2.排除了含0的数。3.优化了启动逻辑。''')

    answerint, answer = generate_unique_number()
    answerlist = list(answer)
    times = 0

    while True:
        times += 1
        print(f'这是您的第 {times} 次猜想。')
        conj = input()
        
        if conj == '0000':
            print(f'太逊了！答案是：{answerint}')
            input('按任意键退出')
            break
        
        if not conj.isdigit() or len(conj) != 4:
            print('输入无效，请输入四位正整数。')
            continue

        result = guess(conj, answerint, answerlist)
        if '666' in result:
            print(f'您赢了！答案是：{answerint}，您共猜了 {times} 次。')
            input('按任意键退出')
            break
        else:
            print(f'您的猜想不正确，其结果是: {result}')

if __name__ == "__main__":
    main()