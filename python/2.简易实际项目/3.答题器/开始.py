
print('Welcome!')
input('Press any key to start.')
choices = []
correct_answers = []
score = 0


with open('question.txt','r',encoding='utf-8') as file:   
    number = 0   # 记录行号
    while True:
        number += 1
        line = str(file.readline())
        if line =='':
            break    # 跳出循环
        else:
            pass

        qa = line.split('$')
        question = qa[0]
        correct_answer = qa[1]

        print(question)

        choice1 = str(input('请输入答案。大小写敏感。'))
        choice2 = choice1 + '\n'

        choices.append(choice1)
        if choice2 == correct_answer:
            score += 1
        correct_answers.append(correct_answer)

print('答题完成,以下为测试结果。')
print('您的答案：',choices)
print('正确答案：',correct_answers,'请您忽略答案中的\\n。')
print('您的分数：',score)
input('任意键退出。')
