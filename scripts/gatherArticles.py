import FeedEntries, RSSFeedArticle, sqlite3

def importNewArticesToDatabase(article, cur, entries, title, image, con):
    for entry in entries:
        try:
            data = ((article(entry).title()), title, image, 
                    article(entry).summary(), article(entry).link(), 
                    article(entry).dayPublished(), article(entry).timePublished())
            
            map(str, data) # making sure every element of data is a string

            cur.execute("""INSERT OR IGNORE INTO 
                           articles(articleTitle, webpageTitle, image, summary, link, dayPublished, timePublished) 
                           VALUES(?,?,?,?,?,?,?)""", data)
        except Exception as e:
            print(f"Error: {e} within {entry}\nthis could be due to a lack of one of the fields.\n{data}")
            pass
    con.commit()

def main():
    with open("../Feeds.txt", "r") as file:
        feeds = [feed.strip() for feed in file]

    article = RSSFeedArticle.FeedArticle
    con = sqlite3.connect("feeds.db")
    cur = con.cursor()

    for feed in feeds:
        entries = FeedEntries.Feed(feed).entries()
        title = FeedEntries.Feed(feed).title()

        try:
            image = FeedEntries.Feed(feed).image()
        except AttributeError:
            image = None

        importArgs = (article, cur, entries, title, image, con)
        importNewArticesToDatabase(*importArgs)

    print("Finished pulling articles.")

if __name__ == '__main__':
    main()