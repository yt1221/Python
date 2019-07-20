weight = float(input('体重を入力してください。'))
height = float(input('身長を入力してください。')) / 100
bmi = weight / (height ** 2)
print(bmi)
if bmi < 18.5:
    print('低体重')
elif 18.5 <= bmi < 25:
    print('標準体重')
elif 25 <= bmi < 30:
    print('前肥満')
elif 30 <= bmi:
    print('肥満')