import sqlite3, gatherArticles, topWordsFromArticle
from json import load, dumps
from internetConnection import connectionIsWorking
from urllib.request import urlopen 
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

sortType = 'All'

def checkSettings():
    f = open("../settings.json")
    return load(f)

def getArticles():
    sortType = open('sortby', 'r').read().replace("\n", "")
    cur = sqlite3.connect("feeds.db").cursor()
    if sortType == 'All':
        cur.execute("select * from articles ORDER BY dayPublished DESC, timePublished DESC;")
    else:
        data = (sortType, )
        cur.execute("select * from articles where webpageTitle = (?) ORDER BY dayPublished DESC, timePublished DESC", data)
    articles = cur.fetchall()
    return articles

def getUnique():
    cur = sqlite3.connect("feeds.db").cursor()
    cur.execute("select distinct webpageTitle from articles;")
    uniqueTitles = cur.fetchall()
    return list(sum(uniqueTitles, ()))

@app.route("/")
def index():
    settings = checkSettings()

    if connectionIsWorking() and settings['check_for_articles_on_refresh'] == "True":
        print("Ping succeeded, pulling articles...")
        gatherArticles.main()

    articles = getArticles()
    uniqueTitles = getUnique()

    return render_template('index.html', articles=articles, settings=settings, uniqueTitles=uniqueTitles) 

@app.route("/changeSort", methods=["GET","POST"])
def changeSort():
    f = open("sortby", "w+")
    if request.method == "POST":
        data = request.get_json()
    f.write(data['name'])
    return dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
