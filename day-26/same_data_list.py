
with open('file_1', 'r') as f:
    file_1 = [i for i in f.readlines()]

with open('file_2', 'r') as f:
    file_2 = [i for i in f.readlines()]
    
check_file = [data.replace('\n', '') for data in file_1 if data in file_2]

print(check_file)