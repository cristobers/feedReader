import sqlite3, gatherArticles
from json import load
from internetConnection import connectionIsWorking
from flask import Flask, render_template

app = Flask(__name__)

def checkSettings():
    f = open("../settings.json")
    return load(f)

def getArticles():
    cur = sqlite3.connect("feeds.db").cursor()
    cur.execute("select * from articles ORDER BY dayPublished DESC, timePublished DESC;")
    articles = cur.fetchall()
    return articles

@app.route("/")
def index():

    settings = checkSettings()

    if connectionIsWorking() and settings['check_for_articles_on_refresh'] == "True":
        print("Ping succeeded, pulling articles...")
        gatherArticles.main()

    articles = getArticles()

    return render_template('index.html', articles=articles, settings=settings) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)