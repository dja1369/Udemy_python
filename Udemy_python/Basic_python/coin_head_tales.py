#동전 던지기를 한다고 가정하고 앞 과 뒤를 나누어서 결정하게 한다

import random

#랜덤레인지의 경우 0 , 1 이 출력된다 그 이유는 2까지 가기 직전까지의 난수를 구하기 때문에 -1 을 해주어야 한다.
coin = random.randrange(2)
#다른 방법
#coin = random.randint(0,1)
print(coin)

if coin == 1:
    print("앞면 입니다!")
else:
    print("뒷면 입니다!")