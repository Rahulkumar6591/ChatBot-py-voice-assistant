import requests
from ss import key  # Ensure 'Key' is defined in ss.py

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + key
json_data = requests.get(api_address).json()

ar = []

def news():
    for i in range(3):  # Loop to get the top 3 news articles
        ar.append("Number " + str(i+1) + ": " + json_data["articles"][i]["title"] + ".")
    return ar  # Return after processing all articles

# arr = news()

# print(arr)
