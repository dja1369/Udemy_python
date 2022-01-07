import random

name_string = input("일행의 이름을 입력하세요!\n")

names = name_string.split(", ")
name_len = (len(names))
roll = names.randint(0, name_len - 1)
print(f"축하해요 이번에 식사값을 계산해줄 사람은 {roll} 입니다!")
