import requests as rq
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "efc2ad89449ba77a3b9f1c1192740371"
parameters = {
    "lat":-12.481090,
    "lon":130.986040,
    "appid":api_key,
    "exclude":"current,minutely,daily",
    "weather":id,

}

response = rq.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data= response.json()
weather_slice = weather_data["hourly"][:12]
for hours_data in weather_slice:
    condition_code =(hours_data["weather"][0]["id"])
    if int(condition_code)<700:
        print("bring an umbrella")
    elif int(condition_code)>=700:
        print("the sky is clear")


#condition = (weather_data["hourly"][0]["weather"][0]["id"])






