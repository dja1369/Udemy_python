import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 조건 상대와 비교하여 내가 이겼는지 확인해야함
game_image = [rock, paper, scissors]
you = int(input("무엇을 내실것인지 선택하여 주세요 0:바위 1:보 2:가위 입니다.\n"))
print("당신의 선택은: ")
print(game_image[you])
#0부터 2까지 범위를 설정 해놨기 때문에 범위 를 한정
computer = random.randint(0,2)
print("컴퓨터의 선택은:")
print(game_image[computer])

if you >= 3 or you < 0:
    print("잘못된 번호를 입력하였습니다")
elif you == computer:
    print("Draw!")
elif you > computer:
    print("you Win!")
elif you == 0 and computer == 2:
    print("you Win!")
elif you == 2 and computer == 0 or you < computer:
    print("you Lose!")
