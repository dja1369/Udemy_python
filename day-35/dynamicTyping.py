# DynamicTyping : 변수의 자료형이 선언시에 정해지는것이 아닌 인터프리터에 의해 유동적으로 결정되는것 
# TypeHine : 변수나 함수의 자료형의 힌트를 제공 > 다른 타입이 들어와도 강제적으로 오류를 발생시키지는 않음 

age: int 
name: str
height: float
is_human: bool

#e.g. 인자를 int로 요청하며, 반환값은 bool값을 요청한다
def driver_license(age: int) -> bool: 
    if age > 18:
        return 'pass!' + True
    else:
        return 'not pass' + False





