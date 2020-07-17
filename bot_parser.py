import requests
from bs4 import BeautifulSoup


class  C1maps:
    def __init__(self, file):
        self.mprint = 0
        self.dos = 0
        self.s = ''
        self.file = file
    def get_data(self):
        result = {}
        vgm_url = 'https://1maps.ru/statistika-koronavirusa-v-rossii-i-mire-na-19-maya-2020-na-segodnyashnij-den/'
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        myFile = open(self.file, 'w')
        with myFile:
            for td in soup.find_all('td'):
                if td.text == 'Москва':
                    self.mprint = 1
                if self.mprint:
                    if self.dos == 0:
                        self.s = td.text
                    if self.dos == 1:
                        self.s += f",{td.text[1:]}\n"
                    self.dos+=1
                    if self.dos == 4:
                        result[self.s.split(",")[0]] = self.s.split(",")[1].replace("\n","")
                        # print(self.s.result)
                        # myFile.write(self.s)
                        self.dos = 0
                        
                        
            return result

    def get_data2(self):
        result = {}
        vgm_url = 'https://koronavirus-ncov.ru/'
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        myFile = open(self.file, 'w')
        with myFile:
            for td in soup.find_all('td'):
                if td.text == 'Великобритания' or td.text == 'Россия':
                    self.mprint = 1
                if self.mprint:
                    if self.dos == 0:
                        self.s = td.text
                    if self.dos == 1:
                        if td.text.find('+') != -1:
                            self.s += f",{td.text.replace(',','')[:(td.text.find('+')-2)]}\n"
                        else:
                            self.s += f",{td.text.replace(',','')}\n"
                    self.dos+=1
                    if self.dos == 6:
                        if self.s.find('Итого'):
                            result[self.s.split(",")[0]] = self.s.split(",")[1].replace("\n","")
                        self.dos = 0
                        
                        
            return result
        
c = C1maps('2maps_covid.csv')
print(c.get_data2())


