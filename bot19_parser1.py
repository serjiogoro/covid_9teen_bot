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
       
        return pic

    def get_info1(self):
        url = 'https://covid19.rosminzdrav.ru/news/'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')        
        h = soup.find_all('a')
        head = []
        for element in h:
            head.append(element.get("href")) 
        return head
    # def get_info2(self):
    #     url = 'https://covid19.rosminzdrav.ru/news/'
    #     req = requests.get(url).text
    #     soup = BeautifulSoup(req, 'html.parser')        
    #     t = soup.find_all('time')
    #     time = []
    #     for element in t:
    #         time.append(element.get("time"))
             
    #     return time   
        



if __name__ == "__main__":
    ParserCov = ParserNews() 
    pic = ParserCov.get_info() 
    head = ParserCov.get_info1()
    # time = ParserCov.get_info2()
    print(pic, head) 
      



