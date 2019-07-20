weight = input('体重を入力してください。')
height = input('身長を入力してください。')
weight = float(weight)
height = float(height) / 100
bmi = weight / (height ** 2)
print(bmi)