import requests 

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status() # 실패한 코드에 대한 예외처리를 자동으로 해줌.

data = response.json()

longitude = data["iss_position"]["longitude"] # 경도
latitude = data["iss_position"]["latitude"] # 위도

iss_position = (longitude, latitude) # 경도, 위도로 이루어진 튜플 생성.


# if response.status_code == 404: # 모든 경우의수를 고려할수 없음
#     raise Exception('Could not found')

# print(response) # response code 반환
# print(response.json()) # JSON 값 반환