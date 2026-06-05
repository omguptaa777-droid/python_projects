import requests
import json


query= input("What type of news you are interested in?")
url= f"https://newsapi.org/v2/everything?q={query}&from=2024-12-19&sortBy=publishedAt&apiKey=6711732980614c7ebab24c76e37c4a80"
r= requests.get(url)

news= json.loads(r.text)

if "articles" in news:
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("----------------------------")
else:
    print("No news articles found in response")