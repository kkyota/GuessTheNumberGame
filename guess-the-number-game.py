import random
min = int(input('最小値を決めてください: '))
max = int(input('最大値を決めてください: '))
def randint(min, max):
 num = int(input('整数を入力してください: '))
 randnum = random.randint(min, max)
 if num == randnum: return True
 else: return False
res = randint(min, max)
print(res)
