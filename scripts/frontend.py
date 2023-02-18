import sqlite3, gatherArticles
from internetConnection import connectionIsWorking
from flask import Flask, render_template

app = Flask(__name__)

def getArticles():
    cur = sqlite3.connect("feeds.db").cursor()
    cur.execute("select * from articles ORDER BY dayPublished DESC, timePublished DESC;")
    articles = cur.fetchall()
    return articles

@app.route("/")
def index():

    if connectionIsWorking:
        print("Ping to 1.1.1.1 successful, internet is working")
        gatherArticles.main()
    else:
        print("Ping to 1.1.1.1 failed, assuming there is no internet connection.")

    articles = getArticles()
    return render_template('index.html', articles=articles) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)