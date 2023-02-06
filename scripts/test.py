import FeedEntries
import RSSFeedArticle
import sqlite3

article = RSSFeedArticle.FeedArticle
con = sqlite3.connect("feeds.db")
cur = con.cursor()

with open("../Feeds.txt", "r") as file:
    feeds = [feed.strip() for feed in file]

def importNewArticesToDatabase(cur, entries, title, image, con):
    for entry in entries:
        try:
            data = (str(article(entry).title()), str(title), str(image), 
                str(article(entry).summary()), str(article(entry).link()), 
                str(article(entry).dayPublished()), str(article(entry).timePublished()))
            cur.execute("INSERT OR IGNORE INTO articles(articleTitle, webpageTitle, image, summary, link, dayPublished, timePublished) VALUES(?,?,?,?,?,?,?)", data)
        except sqlite3.OperationalError as e:
            print(f"{e}")
            pass
    con.commit()
 
def getInformationFromDatabase(cur):
    for row in cur.execute("select * from articles ORDER BY dayPublished DESC, timePublished DESC;"):
        print(row)

def main(feeds, cur, con):
    for feed in feeds:
        entries = FeedEntries.Feed(feed).entries()
        title = FeedEntries.Feed(feed).title()

        try:
            image = FeedEntries.Feed(feed).image()
        except AttributeError:
            image = None

        importNewArticesToDatabase(cur, entries, title, image, con)
        getInformationFromDatabase(cur)

if __name__ == '__main__':
    main(feeds, cur, con)