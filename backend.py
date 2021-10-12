from flask import Flask, render_template
import webscraper



app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/articles")
def articlePage():
    data = webscraper.scrapeESPN()  
    data += webscraper.scrapePackWire()          

    return render_template("articles.html", articles=data)

@app.route("/tweets")
def tweetsPage():
    return render_template("tweets.html")

if __name__ == "__main__":
    app.run()