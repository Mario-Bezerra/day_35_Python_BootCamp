import requests
from twilio.rest import Client

# weather api
END_POINT_API = "https://api.openweathermap.org/data/2.5/onecall?"
API_KEY = "xxxxxxxx"
MY_LAT = -14.861924
MY_LNG = -40.844536

# send SMS api
account_sid = "xxxxxxxxxa"
auth_token = "xxxxxxxx"

# weather params
weather_params = {
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    "exclude": "minutely,daily,alerts,current",
    "appid" : API_KEY
}

# weather request
response = requests.get(END_POINT_API,params=weather_params)
response.raise_for_status()
data_weather = response.json()

will_rain = False

for n in range (12):
    if int(data_weather['hourly'][n]['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's gonna rain. Bring a Umbrella RI-RI ☂️",
        from_='xxxxxx',
        to='xxxxxxxx'
    )
    print(message.status)