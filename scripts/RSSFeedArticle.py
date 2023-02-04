from datetime import datetime

class FeedArticle:
    def __init__(self, article):
        self.article = article

    def title(self):
        return self.article["title"]

    def link(self):
        return self.article["link"]

    def summary(self):
        return self.article["summary"]

    def author(self):
        return self.article["author"]

    def published(self):
        return self.article["published"]
