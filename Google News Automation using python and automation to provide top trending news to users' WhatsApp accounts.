
from GoogleNews import GoogleNews
news = GoogleNews(period='1d')
news.search("India")
result = news.result()

import pandas as pd
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()

for i in result:
    news1 = i["title"]
    news2 = i["desc"]
    news3 = i["link"]

    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read Full News : ", i["link"])
    news = i["title"] +i["desc"] + i["link"]

    print(news)

import pywhatkit
print(i["title"])
print(i["desc"])

pywhatkit.sendwhatmsg('+910000000000',news, 19, 2)
