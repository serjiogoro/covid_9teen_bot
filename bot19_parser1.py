import requests
from bs4 import BeautifulSoup
import re

class ParserNews:
    def __init__(self): 
        self.url = 'https://covid19.rosminzdrav.ru/news/'
        self.req = requests.get(self.url).text
        self.soup = BeautifulSoup(self.req, 'html.parser')

    def get_img(self):
        s = self.soup.find_all("img")
        pic = []
        for element in s:
            pic.append(element.get("src"))
       
        return pic

    def get_href(self):        
        h = self.soup.find_all('a')
        head = []
        for element in h:
            head.append(element.get("href")) 
        return head

    def get_time(self):      
        t = self.soup.find_all('time')
        time = []
        for element in t:
            time.append(element.text)
             
        return time   
        
    def get_heading(self):
        ttl = self.soup.find_all('a')
        heading = []
        for element in ttl:
            heading.append(element.get("title"))

        return heading 

    def get_small_cards(self):
        small_cards = []
        time_array = self.get_time()
        href_array = self.get_href()
        image_array = self.get_img()
        title_array = self.get_heading()

        for heading, href, image, time in zip (title_array, href_array, image_array, time_array,):
            one_card = {}
            descr = self.get_descr(href)
            one_card['title'] = heading
            one_card['image'] = image
            one_card['href'] = href
            one_card['time'] = time
            one_card['descr'] = descr

            small_cards.append(one_card)

        return small_cards

    def get_descr(self,url):
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        tmp = soup.find_all('body')
        descr = tmp[0].text
        descr = re.sub(r'\n+','\n',descr)

        return descr






if __name__ == "__main__":
    ParserCov = ParserNews() 
    pic = ParserCov.get_img() 
    head = ParserCov.get_href()
    time = ParserCov.get_time()
    heading = ParserCov.get_heading()
    descr = ParserCov.get_descr(url='https://covid19.rosminzdrav.ru/minzdrav-rossii-napravit-speczialistov-v-tyvu-v-svyazi-so-vspyshkoj-covid-19/')
    small_cards = ParserCov.get_small_cards()
    print(small_cards)

      



