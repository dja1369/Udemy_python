# dictionary comprehension 
# new_dict = {new_key : new_value for item in list} 기본 틀
# new_dict = {new_key : new_value for key, value in dict.items()}
# new_dict = {new_key : new_value for key, value in dict.items() if 조건}
import random
names = ['Alex', 'Beth', 'Carolune', 'Dave', 'Eleanor', 'Freddie']

new_dict = {name : random.randint(1,100) for name in names} # 딕셔너리 컴프리헨션 

pass_dict = {name : score for name, score in new_dict.items() if score > 60} # 딕셔너리 컴프리헨션에 조건 추가 

print(pass_dict) 

''' 단어 길이 체크 하여 사전형으로 반환 하기 '''
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

wording = sentence.split()

sentence_dict = {word : len(word) for word in wording}

print(sentence_dict)

# 더 간단한 방법 
# sentence_dict = {word : len(word) for word in sentence.split()}


''' 날짜 별 온도를 C에서 F로 변경하기 '''
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key : ((value * 9 / 5) + 32) for key, value in weather_c.items()}

print(weather_f)


# 판다스 데이터프레임에서 반복 받는법 

import pandas as pd

student_dict = {
    'student' : ['Alex', 'Beth', 'Carolune'],
    'score' : [57,70,95]
}

student_dataframe = pd.DataFrame(student_dict)

print(student_dataframe)
print()
print()
for k, v in student_dataframe.items(): # 이는 단순히 행의 반복만을 의미한다 
    print(f"k : {k}"
          f'v : {v}')


print()
print()    
for index, row in student_dataframe.iterrows():
    print(f"index : {index}" , f' row : {row}')
    # print(row.student) , print(row.score) 행에서의 학생만 출력, 행에서의 점수만 출력도 가능하다.