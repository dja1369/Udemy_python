#리스트는 많은 자료를 []대괄호에 저장할수있으며 자료형에 상관없이 혼합된 데이터도 저장이 가능하다.
#순서도 중요하다 순서가 저장되기에 순서에 맞게 기입하여야 한다.
city_of_korea = ["서울", "부산", "대구", "울산", "대전", "광주", "인천"]

print(city_of_korea)
print(city_of_korea[0])

city_of_korea.append("덕수 도시")
print(city_of_korea)
#여러개를 리스트의 끝에 추가 가능 이경우 리스트 로 입력
city_of_korea.extend(["재석 도시", "명수 도시"])