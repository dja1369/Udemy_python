import pandas as pd 

#TODO 1. csv파일을 읽어와 사전형으로 매핑 
nato_csv = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {}
for index, row in nato_csv.iterrows():
    nato_dict[row.letter] = row.code
    
#TODO 2. 단어나 이름을 입력받아 NATO WORD로 변경
words = input('input your name here! : ')

word = [nato_dict[s.upper()] for s in words]

print(word)