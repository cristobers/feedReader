import feedparser

class Feed:
    
    def __init__(self, url):
        self.url = url
        try:
            self.feed = feedparser.parse(url)
        except Exception as e:
            print(f"An error occured when trying to gather articles: {e}")  

    def entries(self):
        return self.feed["entries"]

    def title(self):
        return self.feed.feed.title

    def image(self):
        return self.feed.feed.image.href