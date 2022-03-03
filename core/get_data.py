from requests_html import HTMLSession


class getHTML:
    def __init__(self, url):
        self.url = url
        self.html = self.getHTML()
        self.soup = self.getSoup()

    def getHTML(self):
        session = HTMLSession()
        try:
            r = session.get(self.url)
            if r.status_code == 200:
                return r.text
            else:
                raise Exception("Error: SOmething went wrong\nStatus Code:", r.status_code)
        except:
            return False

    def getSoup(self):
        from bs4 import BeautifulSoup

        try:
            return BeautifulSoup(self.html, "html.parser")
        except:
            return False
