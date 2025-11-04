import requests
import os
import json
import webbrowser
from dotenv import load_dotenv #to access the env variables in this file


#load the env variables from the .env files
load_dotenv() #method call/loads .env file
#access env variables
api_key= os.getenv('X-RapidAPI-Key')
news_api_key=os.getenv('NEWS_API')
current_news_api=os.getenv("API_KEY_CURRENT")
#example usage
print(f"api key:{current_news_api}")
print(f"NEWS key:{news_api_key}")


# user function to get weather updates nd news
def weather_and_news(city):

    #city=input("enter upur city please: ")


    # current weather api
    url='https://api.openweathermap.org/data/2.5/weather'
    params={"q":f"{city}","appid":current_news_api,"units":"metric"}
    response=requests.get(url,params=params)
    response=response.json()
    print(response)
    name=response['name']
    condition=response['weather'][0]['description']
    temp=response['main']['temp']
    #for weather map,extracting coordinates of the city
    lat=response['coord']['lat']
    lon=response['coord']['lon']
    

    # weather news api Call with query=city + weather
    url2="https://gnews.io/api/v4/search"
    params={
        "q":f"{city} weather", #it takes q/what to search for
        "lang":"en",
        "max":5,
        "apikey":news_api_key

    }
    response1=requests.get(url2,params=params).json()
    #print(response1)
    title=response1['articles'][0]['title']
    warning=response1['articles'][0]['description']
    related_news= title+ ". " + warning


    #openweathermap api call for map
    url3=f"https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat={lat}&lon={lon}&zoom=7" #use f-string to insert lat nd lon values
    response2=requests.get(url3) #requests cant return an image object, only response obj
    webbrowser.open(url3) #to view the map in browser
    
    
    data={
        "city":name,
        "tempreture":f"{temp}C",
        "condition":condition,
        "related_news":related_news,
        "temp_map":url3
        
        }
    # print each key on a new line
    print(json.dumps(data,indent=4))
    return data

