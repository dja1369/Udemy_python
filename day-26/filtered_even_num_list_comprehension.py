# list_comprehension을 이용하여 짝수값 추출 

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_numbers = [num for num in numbers if num % 2 == 0 ]

print(even_numbers)