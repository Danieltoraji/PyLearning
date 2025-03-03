import random
k = int(input('输入k值'))
n = int(input('输入n值'))

def calc(k,n):
    bestscore = -1
    output = 0
    numberlist = random.sample(range(n),n)
    for i in range(k):
        if numberlist[i] > bestscore:
            bestscore = numberlist[i]
        else:
            pass
    for i in range(k,n):
        if i > bestscore:
            output = i
            break
        else:
            pass
    if bestscore == n-1:
        return False
    elif output == n-1:
        return True
    else:
        return False


success = 0
count = 1
while count <= 1000:
    count += 1
    print(count)
    if calc(k,n) == True:
        success += 1
    else:
        pass

print('实验成功了：',success,'次')
