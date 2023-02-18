import sqlite3, gatherArticles
from flask import Flask, render_template


def getArticles():
    cur = sqlite3.connect("feeds.db").cursor()
    cur.execute("select * from articles ORDER BY dayPublished DESC, timePublished DESC;")
    articles = cur.fetchall()
    return articles

app = Flask(__name__)
@app.route("/")
def index():
    gatherArticles.main()
    articles = getArticles()
    return render_template('index.html', articles=articles) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)