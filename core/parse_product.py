from bs4 import BeautifulSoup
from get_data import getHTML


class parseProduct:
    def __init__(self):
        self.url = "https://www.amazon.in/s?k=samsung"
        self.data = getHTML(self.url).html
        self.result = []


    def getData(self):
        if self.data is not False:
            """"""
            soup = BeautifulSoup(self.data, 'html.parser')


            scraped_devices = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
            for vals in scraped_devices:
                # self.result.append(vals.contents[0])
                temp = vals.contents[0]
                if temp.startswith("Samsung"):
                    self.result.append(temp)
                else:
                    print("Huh, that's not a samsung phone")
            return self.result