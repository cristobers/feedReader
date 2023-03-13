import sqlite3, os

def DatabaseExists():
    if os.path.exists("feeds.db"):
        return True
    return False

def createDatabase():
    connection = sqlite3.connect("feeds.db")
    cur = connection.cursor()
    return cur

def main():
    if not DatabaseExists():
        createDatabase().execute("CREATE TABLE articles(articleTitle PRIMARY KEY , webpageTitle , image, summary, link , dayPublished DATE, timePublished TIME, articleText)")
        return
    print("feeds.db already exists")

if __name__ == '__main__':
    main()