# 금액을 계산하고 팁을 계산하는 프로그램

price = int(input("금액을 입력하세요: "))
members = int(input("일행을 입력하세요: "))
send_a_tip = int(input("팁을 얼마나 주시겠습니까? 10, 12, 15: "))

calc = price / members
tips = round(price * (send_a_tip / 100),2)

print ("{0}인이서 내야할 금액은 {1} 달러 이며 팁은 {2} 입니다!".format(members,calc,tips))