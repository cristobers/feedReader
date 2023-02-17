import sqlite3
from flask import Flask, render_template
# https://stackoverflow.com/questions/66995362/can-i-add-elements-to-an-html-page-using-flask

def getArticles():
    con = sqlite3.connect("feeds.db")
    cur = con.cursor()
    cur.execute("select * from articles ORDER BY dayPublished DESC, timePublished DESC;")
    articles = cur.fetchall()
    return articles

app = Flask(__name__)
@app.route("/")
def index():
    articles = getArticles()
    return render_template('index.html', articles=articles) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)