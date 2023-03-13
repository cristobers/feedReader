
class FeedArticle:
    def __init__(self, article):
        self.article = article

    def title(self) -> str:
        return self.article["title"]

    def link(self) -> str:
        return self.article["link"]

    def summary(self) -> str:
        return self.article["summary"]

    def author(self) -> str:
        return self.article["author"]

    def published(self):
        return self.article["published"]

    def dayPublished(self) -> str: # SQL formats its dates as: YYYY-MM-DD
        date = f"{self.article.updated_parsed.tm_year}-{str(self.article.updated_parsed.tm_mon).zfill(2)}-{str(self.article.updated_parsed.tm_mday).zfill(2)}"
        return date

    def timePublished(self) -> str:
        time = f"{str(self.article.updated_parsed.tm_hour).zfill(2)}:{str(self.article.updated_parsed.tm_min).zfill(2)}:{str(self.article.updated_parsed.tm_sec).zfill(2)}"
        return time
    