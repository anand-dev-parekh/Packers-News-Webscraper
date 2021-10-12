import requests
from bs4 import BeautifulSoup
from articleClass import Article      




def scrapeESPN():
    r = requests.get("https://www.espn.com/nfl/team/_/name/gb/green-bay-packers")

    soup = BeautifulSoup(r.content, "lxml")
    finder = soup.find("div", class_="main-content layout-abc")


    container = finder.find("div", class_="container")
    articles = container.find_all("article")

    data = []

    for article in articles:
    
        try:
            info = article.find("div", class_="item-info-wrap")

            title = info.h1.a.text
            description = info.p.text
            time = info.span.text

            if article.a['href'][0:4] == "/nfl":
                url = "https://www.espn.com" + article.a['href']
            elif article.a['href'][0:5] == "/blog":
                url = "https://www.espn.com" + article.a['href']
            else:
                url = article.a['href']


            object = Article(title, time, description, url)
            data.append(object)

        except AttributeError:
            pass
    return data


def scrapePackWire():
    r2 = requests.get("https://packerswire.usatoday.com/")
    soup2 = BeautifulSoup(r2.content, "lxml")
    articles2 = soup2.find_all("div", class_="post post--stream")
    data = []

    for article2 in articles2:
        try:
            title2 = article2.span.h3.a.text
            description2 = "NA"

            timeHTML = article2.find("span", "post__date")

            timeStampData = timeHTML.text.split(" ")

            if timeStampData[1] == "hours":
                time2 = timeStampData[0] + "h"
            elif timeStampData[1] == "days" or timeStampData[1] == "day":
                time2 = timeStampData[0] + "d"
            elif timeStampData[1] == "minutes":
                time2 = timeStampData[0] + "min"

            url2 = article2.span.h3.a["href"]

            object = Article(title2, time2, description2, url2)
            data.append(object)

        except AttributeError:
            pass
    return data