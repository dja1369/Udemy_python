 
 # new_list = [new_item for item in list] 리스트 컴프리헨션 기본 틀 
 # new_list = [new_item for item in list if 조건] 리스트 컴프리헨션 조건문 기본 틀
 # python의 sequences 종류 list, range, string, tuple 
 # sequences는 값이 연속적으로 이어진것을 의미한다 
 # e.g.
new_list = [i+1 for i in range(1,4)]
print(f"new_list : {new_list}")


name = 'james'
name_list = [string for string in name]

print(f"name_list : {name_list}")

range_challenge = list(range(2,10,2)) #list 형식으로 생성 
range_challenge = [i for i in range(2,10,2)] # list_comprehension 형식으로 생성

print(f"range_challenge : {range_challenge}")