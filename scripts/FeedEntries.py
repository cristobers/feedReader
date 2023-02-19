import feedparser

# The parsed articles want to end up in a .sql database
# from which we can place them into the Flask frontend.
# This is going to be called from many different places.

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