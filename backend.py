from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/articles")
def articlePage():
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

            data.append([title, time, description, url])
            
        except:
            pass

    r2 = requests.get("https://packerswire.usatoday.com/")
    soup2 = BeautifulSoup(r2.content, "lxml")
    articles2 = soup2.find_all("div", class_="post post--stream")

    for article2 in articles2:
        try:
            title2 = article2.span.h3.a.text
            description2 = "NA"

            timeHTML = article2.find("span", "post__date")

            timeStampData = timeHTML.text.split(" ")

            if timeStampData[1] == "hours":
                time2 = timeStampData[0] + "h"
            elif timeStampData[1] == "days":
                time2 = timeStampData[0] + "d"
            elif timeStampData[1] == "minutes":
                time2 = timeStampData[0] + "min"

            url2 = article2.span.h3.a["href"]


            data.append([title2, time2, description2, url2])

        except:
            pass


    return render_template("articles.html", articles=data)

@app.route("/tweets")
def tweetsPage():
    return render_template("tweets.html")

app.run()