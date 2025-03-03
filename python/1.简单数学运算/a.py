print('欢迎使用原神伤害计算系统-内测版！')
input('按enter开始计算。')

atk_basic = int(input('基础攻击力'))
atk_green = int(input('绿色攻击力'))
print('接下来计算追加攻击力。选择加成：')
while True:
    atk_append_choice = input('''
    选择加成：
    1.班尼特大招(13级)    2.锅巴朝天椒    3.美味的仙跳墙(372,12)   4.退出
    ''')
    if atk_append_choice == '1':
        atk_bennett = int(input('班尼特白字：')) * 1.03
    if atk_append_choice == '2':
        atk_guoba = atk_basic * 0.15
    if atk_append_choice == '3':
        atk_food = int(372)
        xiantiaoqiang = 1
        print('暴击率加成将自动计入。')
    if atk_append_choice == '4':
        print('当前加成为：',
        '1.班尼特：',atk_bennett,
        '2.锅巴：',atk_guoba,
        '3.食物：',atk_food,'请确认。1:正确;2:修改。')
        atk_confirm = input()
        if atk_confirm == '1':
            atk_total = atk_basic + atk_green + atk_bennett + atk_guoba + atk_food
            break
        if atk_confirm == '2':
            print('请返回修改数据。修改后的数据将覆盖之前的。')
            pass
        else:
            pass
    else:
        pass

#定义倍率库
skill_list = ['神里绫华-重击','神里绫华-霜灭-切割','神里绫华-霜灭-绽放','神里绫华-冰华','雷电将军-Q后首刀-0愿力','雷电将军-Q后首刀-满愿力','宵宫-普通攻击5-E技能后']
skill_number = ['11','12','13','14','21','22','31']
skill_dmg = [3.27,2.02,3.03,4.31,7.21,11.41,3.054513]

for x in range(len(skill_number)):
    print(skill_number[x],skill_list[x])
