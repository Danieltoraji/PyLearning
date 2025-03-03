import random
t = 0
uu = list("chinese")
tw = len(uu) - 1
with open('res.txt','a') as f:
    while True:
        s = random.randint(0,tw)
        ss = uu[s]
        t += 1
        print(ss,t)
        f.write(ss)
