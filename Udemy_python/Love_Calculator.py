#이번 연습은 사랑 계산기 입니다.
print("welcome to the Love Calculator")
his_name = input("What is your Name? : \n")
her_name = input("What is their Name : \n")

joined_name = his_name + her_name
lower_change = joined_name.lower()
t = lower_change.count("t")
r = lower_change.count("r")
u = lower_change.count("u")
e = lower_change.count("e")

true = t+r+u+e

l = lower_change.count("l")
o = lower_change.count("o")
v = lower_change.count("v")
e = lower_change.count("e")

love = l+o+v+e


#better method
#love_score = int(str(true) + str(love))
love_score = str(true) + str(love)

print(f"love score is {love_score}")
innteger = int(love_score)

if 10 > innteger or innteger > 90:
    print("Like buring love")
elif 50 >= innteger >= 40:
    print("fine Friend")

