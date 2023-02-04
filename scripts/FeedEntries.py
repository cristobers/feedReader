import feedparser

# The parsed articles want to end up in a .sql database
# from which we can place them into the Flask frontend.
# This is going to be called from many different places.

class Feed:
    
    def __init__(self, url):
        self.url = url
        self.feed = feedparser.parse(url)

    def entries(self):
        return self.feed["entries"]

    def title(self):
        return self.feed.feed.title

    def image(self):
        return self.feed.feed.image.href