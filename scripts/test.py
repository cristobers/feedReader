import FeedEntries
import RSSFeedArticle
import sqlite3

article = RSSFeedArticle.FeedArticle
con = sqlite3.connect("feeds.db")
cur = con.cursor()

with open("../Feeds.txt", "r") as file:
    feeds = [feed.strip() for feed in file]

for feed in feeds:
    entries = FeedEntries.Feed(feed).entries()
    title = FeedEntries.Feed(feed).title()

    try:
        image = FeedEntries.Feed(feed).image()
    except AttributeError:
        image = None

    for entry in entries:
        data = (str(article(entry).title()), str(title), str(image), str(article(entry).summary()), str(article(entry).link()), str(article(entry).published()))
        cur.execute("INSERT OR IGNORE INTO articles(articleTitle, webpageTitle, image, summary, link, published) VALUES(?,?,?,?,?,?)", data)
    con.commit()