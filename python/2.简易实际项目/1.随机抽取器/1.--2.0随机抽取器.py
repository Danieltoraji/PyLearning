#              小呆随机抽取器          制作者:Daniel
#----------需要临时添加名单版本------Ver:2.0---最后更新于2022.1.30----------------------------------------------------------
print('欢迎使用小呆随机抽取器!')
name_list = []

#添加
while 4 > 3:
    add_element_name = input('输入要添加的元素~')
    name_list.append(add_element_name)
    print('已有名单:',name_list)
    add_element_situation = input('添加成功，是否继续输入？输入Y或y继续，回车停止。')
    if add_element_situation == 'Y':
        pass
    elif add_element_situation == 'y':
        pass
    else:
        break

#修改
while 4 > 3:
    print(name_list)
    change_situation = input('请确认是否正确。Y表示正确，回车键修改。')
    if change_situation == 'Y':
        break
    else:
        while 4 > 3:
            change_choice = input('正在修改列表。继续添加输入1，删除输入2，更改输入3,退出输入4。')
            if change_choice == '1':
                while 4 > 3:
                    add_element_name = input('输入要添加的元素~')
                    name_list.append(add_element_name)
                    print('已有名单:',name_list)
                    judge1 = input('添加成功，是否继续输入？输入Y或y继续，回车停止。')
                    if judge1 == 'Y':
                        pass
                    elif judge1 == 'y':
                        pass
                    else:
                        break
            if change_choice == '2':
                while 4 > 3:
                    print('已有名单:',name_list)
                    del_element_num = int(input('输入第几个元素'))
                    del name_list[del_element_num - 1]
                    print('完成!已有名单:',name_list)
                    judge2 = input('删除成功，是否继续输入？输入Y或y继续，其他任意字符停止。')
                    if judge2 == 'Y':
                        pass
                    elif judge2 == 'y':
                        pass
                    else:
                        break
            if change_choice == '3':
                while 4 > 3:
                    print('已有名单:',name_list)
                    replace_element_num = int(input('更改第几个元素?'))
                    replace_element_element = input('更改为?')
                    name_list[replace_element_num - 1] = replace_element_element
                    print('完成!已有名单:',name_list)
                    judge3 = input('更改成功，是否继续输入？输入Y或y继续，其他任意字符停止。')
                    if judge3 == 'Y':
                        pass
                    elif judge3 == 'y':
                        pass
                    else:
                        break
            if change_choice == '4':
                break
            else:
                pass

#参数输入
print('当前列表:',name_list)
times = input('输入抽取个数:')
input('按下回车继续')
sum_element_num = len(name_list) - 1

#抽取
import random
already_done = 0
while 4 > 3:
    result_num = (random.randint(0, sum_element_num))
    already_done += 1
    print(already_done,'号,',name_list[result_num])
    if already_done == int(times):
        break

input('抽取完成!回车退出。')