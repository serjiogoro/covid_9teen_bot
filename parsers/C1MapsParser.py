import requests
from bs4 import BeautifulSoup

class  C1maps:
    def __init__(self):
        self.mprint = 0
        self.dos = 0
        self.s = ''
    def getRusData(self):
        vgm_url = 'https://1maps.ru/statistika-koronavirusa-v-rossii-i-mire-na-19-maya-2020-na-segodnyashnij-den/'
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        contries = {}
        for td in soup.find_all('td'):
            if td.text == 'Москва':
                self.mprint = 1
            if self.mprint:
                if self.dos == 0:
                    self.s = td.text
                if self.dos == 1:
                    self.s += ',' + td.text[1:] + '\n'
                self.dos+=1
                if self.dos == 4:
                    contries[self.s.split(',')[0]] = int(self.s.split(',')[1])
                    self.dos = 0
                    self.s = ''
        sorted_contries = sorted(contries.items(),  key=lambda x: x[1], reverse=True)
        return sorted_contries

    def getWorldData(self):
        vgm_url = 'https://koronavirus-ncov.ru/'
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        contries = {}
        for td in soup.find_all('td'):
            if td.text == 'Великобритания' or td.text == 'Россия':
                self.mprint = 1
            if self.mprint:
                if self.dos == 0:
                    self.s = td.text
                if self.dos == 1:
                    if td.text.find('+') != -1:
                        self.s += ',' + td.text.replace(',','')[:(td.text.find('+')-2)] #+ '\n'
                    else:
                        self.s += ',' + td.text.replace(',','')# + '\n'
                self.dos+=1
                if self.dos == 6:
                    if self.s.find('Итого') == -1 & self.s.find('Европа') == -1:
                        contries[self.s.split(',')[0]] = int(self.s.split(',')[1])
                    self.dos = 0
                    self.s = ''
        sorted_contries = sorted(contries.items(),  key=lambda x: x[1], reverse=True)
        return sorted_contries

#c = C1maps()
#c.getRusData()
#l = c.getRusData()
#for key, value in l:
#    print(key + '->' + str(value)+ '\n')