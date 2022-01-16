#Lotto.py

import random

num = int(input("Lotto 게임수를 입력 하세요:"))

print("Lotto 자동 번호 입니다.")
print("꼭 좋은결과 얻길 바랍니다 by이덕수")
print("-----------------------------")

#입력한 게임수 만큼 반복
for x in range(num):
    Lotto = [0,0,0,0,0,0]

    Lotto[0] = random.randrange(1,46)

    Lotto[1] = Lotto[0]
    Lotto[2] = Lotto[0]
    Lotto[3] = Lotto[0]
    Lotto[4] = Lotto[0]
    Lotto[5] = Lotto[0]

    while (Lotto[0] == Lotto[1]):
        Lotto[1] = random.randrange(1,46,1)
    while (Lotto[0] == Lotto[2] or Lotto[1] ==[2]):
        Lotto[2] = random.randrange(1,46,1)
    while (Lotto[0] == Lotto[3] or Lotto[1] == Lotto[3] or
           Lotto[2] == Lotto[3]):
        Lotto[3] = random.randrange(1,46,1)
    while (Lotto[0] == Lotto[4] or Lotto[1] == Lotto[4] or
           Lotto[2] == Lotto[4] or Lotto[3] == Lotto[4]):
        Lotto[4] = random.randrange(1,46,1)
    while (Lotto[0] == Lotto[5] or Lotto[1] == Lotto[5] or
           Lotto[2] == Lotto[5] or Lotto[3] == Lotto[5] or
           Lotto[4] == Lotto[5]):
        Lotto[5] = random.randrange(1,46,1)

    Lotto.sort()

    print("[%2d,%2d,%2d,%2d,%2d]" % (Lotto[0],Lotto[1],Lotto[2],Lotto[3],Lotto[4]))
nu = int(input("로또에 너무 빠지지 않게 조심하세욧!"))    
