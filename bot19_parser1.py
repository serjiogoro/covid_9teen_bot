import requests
from bs4 import BeautifulSoup

class ParserNews:
    def __init__(self):
        self.url = 'https://covid19.rosminzdrav.ru/news/' 

    def get_info(self):
        url = 'https://covid19.rosminzdrav.ru/news/'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')
        s = soup.find_all("img")
        pic = []
        for element in s:
            pic.append(element.get("src"))
        h = soup.find_all("title")
        head = []
        for element in h:
            head.append(element.get("href")) 
        t = soup.find_all("time")
        time = []
        for element in t:
            time.append(element.get("time"))
             

        return pic, head, time   
        



if __name__ == "__main__":
    ParserCov = ParserNews() 
    pic = ParserCov.get_info() 
    head = ParserCov.get_info()
    time = ParserCov.get_info()
    print(pic, head, time) 
      



