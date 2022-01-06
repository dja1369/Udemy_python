# 표준 체중을 구하는 프로그램
# 공식 : 남자 키 * 키 * 22
#       여자 키 * 키 * 21
# 조건 1: 표준 체중은 별도의 함수 내에서 게산
#             함수명 : std_weight
#             전달값 : 키(height) , 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리까지 표시
#
# (출력 예제)
# 키 175 남자의 표준 체중은 67.38KG 입니다.

def std_weight(height, gender):
    if gender == "man":
        calc = height * height * 22 / 10000
        print("키",height,"남성의 몸무게는{:.2f}kg".format(calc))
    elif gender == "woman":
        calc = height * height * 21 / 10000
        print("키",height,"여성의 몸무게는{:.2f}kg".format(calc))

#round(단위,자릿수) 를 이용하여 구현 하여도 됨  
std_weight(175, "man")