
# 90살 까지 살수있다고 가정한후 현재 나이 부터 미래의 사망일 까지 의 남은 일수를 계산해주는 프로그램

age = input("당신의 현재 나이는 몇살인가요? \n")

die_day = (age - 90) * 365
die_hour = die_day * 24
die_month = (90 - age)