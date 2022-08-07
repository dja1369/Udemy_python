import requests
# 위도, 경도 url : https://www.latlong.net/
# 현재는 OnecallAPI가 유료로 바뀌어 사용하려면 구독을 해야함.

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "your_api_key"

weather_params = {
    "lat" : 37.484001,
    "lon" : 126.929776,
    "appid" : api_key,
}

resp = requests.get(OWN_Endpoint, params = weather_params)

print(resp.status_code)
print(resp.text)