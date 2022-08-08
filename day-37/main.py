import requests 
import datetime

USERNAME: str = "ducks"
TOKEN = "pixelatoken"
GRAPHID = "graphsid"
TODAY = t = datetime.date.today().strftime("%Y%m%d")
headers ={
    "X-USER-TOKEN" : TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

'''
계정 생성 
토큰, 유저이름, 서비스동의여부, 성인여부
'''
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

resp = requests.post(url = pixela_endpoint, json = user_params)

# print(resp.status_code)
# print(resp.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

'''
그래프 생성 
ID, GraphName, 단위, 자료형
색 종류 : shibafu(녹색), momiji(red), sora(blue), ichou(yellow), ajisai(purple), kuro(black)
'''
graph_config = {
    "id" : GRAPHID,
    "name" : "Daily Habit Trackers",
    "unit" : "CommitCount",
    "type" : "int",
    "color" : "shibafu"
}

resp = requests.post(url = graph_endpoint, json = graph_config, headers = headers)

# print(resp.status_code)
# print(resp.text)

addpixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

'''
픽셀 추가 
date: STR, format: yyyyMMdd
quantity: STR, 추가할 양 
'''
addpixel_config = {
    "date" : TODAY,
    "quantity" : input("오늘 몇번의 Commit을 하셨나요 : ")
}

resp = requests.post(url = addpixel_endpoint, json = addpixel_config, headers = headers)
# print(resp.status_code)
# print(resp.text)

updatepixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{TODAY}"

'''
픽셀 업데이트 
quantity: STR, 추가할 양 
'''
updatepixel_config = {
    "quantity" : input("업데이트 한 Commit의 수를 입력 해주세요 : ")
}

resp = requests.put(url = updatepixel_endpoint, json = updatepixel_config, headers = headers)

print(resp.status_code)
print(resp.text)


# 업데이트와 동일한 URL을 재사용
resp = requests.delete(url = updatepixel_endpoint, headers = headers)

print(resp.status_code)
print(resp.text)

 