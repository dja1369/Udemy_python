money = [cash]

menu = 0

while menu !=4:
#메뉴가 9일때 돌아가려면 ==이지만 이건 아닐때 계속 반복해야 하므로 !=가 된다
    print('------------------------------')
    print('1. 잔액조회')
    print('2. 입금')
    print('3. 인출')
    print('4. 종료')

    menu = int(input('메뉴를 선택하시오:'))

    #메뉴 기능 넣기
    #1번 메뉴 는 = 리스트 출력
    if menu ==1:
        print('입금')
        money.append(cash)
    #2번 메뉴 는 = 리스트 추가
    elif menu ==2:
       name = input('입금할 금액을 입력하세요')
    #3번 메뉴 는 = 리스트 삭제
    elif menu ==3:
       del_cash = input('인출할 금액을 입력하세요')

       if del_cash in money:

           money.remove(del_cash)
           print('출금 되었습니다^^')

       else:

           print('잔액 부족입니다ㅠㅠ')
    
