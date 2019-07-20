import random

num = random.randint(0,9)

i = 0

while i < 5:
    answer = input('0から9の数字を入力してください。')

    if  not answer.isdigit():
        print('数字を入力してください')

    else:
        
        if int(answer) == num:
            i = i + 1
            print('正解')
            break
        else:
            print('不正解')
            i = i + 1

if i == 5:
    print('残念でした、また挑戦してね')
elif i < 5:
    print('あなたの挑戦回数は' + str(i) + '回です。')