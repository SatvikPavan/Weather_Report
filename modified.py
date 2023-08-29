import requests
from datetime import datetime
from twilio.rest import Client

user_api=input("Enter the user's API key")
location = input("Enter the city name:")

api_endpoint = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(api_endpoint)
data=api_link.json()

if data['cod'] == '404':
    print("Invalid city: {}, please check your city name".format(location))
else:
    temperature = ((data['main']['temp'])-273)
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p")
    print("----------------------------------------------------")
    print("Weather stats for - {} || {}".format(location.upper(), date_time))
    print("----------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temperature))
print("Current weather description :",weather_description)
print("Current Humidity  :",humidity,'%')
print("Current wind speed  :",wind_speed,'kmph')

account_sid = input("Enter user's account number.")
auth_token = input("Enter user's auth token.")

# If rain comes in user entered location then a message is sent in to user's mobile number using twilio API.
if data["weather"][0]['id'] < 700 :
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+19285850644',
        body="It's going to rain today, Remember to bring umbrella",
        to='+919441899599'
    )
    print(message.sid)






