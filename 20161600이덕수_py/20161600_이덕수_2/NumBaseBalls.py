# Up_and_doun_game.py
import random

r_num = random.randrange(1, 101)
num = 0
try_count = 0

try:
    print("반갑습니다 이게임의제작자 인 이덕수 입니다!!!")
    print("1~100 숫자 Up & Down 게임을 시작합니다 !!!")
    print("=============================================")

    while (r_num != num):

        num = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))

        if (num > r_num):
            print("Down")
        elif (num < r_num):
            print("Up")

        try_count = + 1

        print("==========================================")
    print(try_count, "번 만에 정답을 맞추셨습니다")

except Exception as e:
    print(e)
