import sys

# end는 끝을 선택한 단어로 바꿔줌 Python은 자동으로 줄바꿈이 되어있기에 밑의 문장은 이어져서 나오게 됨
print("Python", "Java", "JavaScript", sep=" vs ", end="?")
print("\n무엇이 더 재밌을까요")

# out은 표준 출 err은 표준 에러
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)


# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    # ljust은 왼쪽 정렬 ()는 얼마나 거리를 잡을것인지
    # rjiust는 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    # zfilld은 정해진 값 만큼 0으로 채우는것
    print("대기번호 : " + str(num).zfill(3))

# answer = input("아무값 이나 입력하세여 :")
# print("입력하신 값은 {0}입니다 ".format(answer))

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >-10}".format(500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000))
# 3자리 마다 콤마를 찍어주고 ,+-부호도 붙이기
print("{0:+,}".format(100000000))
print("{0:-,}".format(100000000))
# 3자리 마다 콤마를 찍어주고, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000))
# 소수점 출력
print("{0:f}".format(5 / 3))
# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5 / 3))
