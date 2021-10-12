class Article:
    def __init__(self, title, time, description, url):
        self.title = title
        self.time = time
        self.description = description
        self.url = url

    def getTitle(self):
        return self.title
    def getTime(self):
        return self.time
    def getDescription(self):
        return self.description
    def getURL(self):
        return self.url 