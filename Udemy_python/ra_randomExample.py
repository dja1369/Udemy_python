#import my_module
import random

#1부터 10사이 랜덤으로 정수값 호출
random_integer = random.randint(1, 10)
print(random_integer)
#코드를 다른데서 작성하여 모듈 식으로 부착 가능
#print(my_module.pi)

#0.0 ~ 1.0 사이의 랜덤 실수값 호출
random_float = random.random()
print(random_float)
#만약 1.0~5.0 까지의 랜덤 실수값을 호출하고 싶다면 어떻게 해야할까?
#랜덤.유니폼은 실수의 범위를 생성 가능하다!
random_large = random.uniform(1,5)
print(random_large)
#이를 응용하여 바로 전 프로그램인 사랑 계산기를 쉽게 변경할수 있다
love_score = random.randint(1,100)
print(f"당신의 사랑 점수는 {love_score}% 입니다!")