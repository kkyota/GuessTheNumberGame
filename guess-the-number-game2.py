import random
minnum = int(input('最小値を決めてください: '))
maxnum = int(input('最大値を決めてください: '))
def randint(minnum, maxnum):
 num = int(input('整数を入力してください: '))
 randnum = random.randint(minnum, maxnum)
 if num == randnum: return True
 else: return False

for i in range(10):
    res = randint(minnum, maxnum)
    print(res)