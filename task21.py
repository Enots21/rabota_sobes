import csv

import requests
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/cheboksary/kvartiry/prodam/1-komnatnye/novostroyka-ASgBAgICA0SSA8YQ5geOUsoIgFk'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

if r.status_code == 200:
    r.encoding = 'utf-8'
    print('Получено успешно')
else:
    print('Ошибка')

table = soup.find_all('div', attrs={'class': 'iva-item-titleStep-zichc'})
table_money = soup.find_all('div', attrs={'class': 'price-price-j2OjU'})

tab = [ari.text for ari in table]
tab_money = [ari.text for ari in table_money]

with open('task21.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('Количество комнат', 'Площадь', 'Этаж', 'Цена'))
    for i, k in zip(tab, tab_money):
        data = i.split()  # раздебиваем строку по пробелам
        rooms = data[0] + data[1].replace(',', '')  # количество комнат
        quadrature = data[2]  # количество кв.м
        floor = data[4].replace('', '')  # этаж
        summa = k.replace(',', '')  # сумма
        writer.writerow((rooms, quadrature, floor, summa))
print('Работа готова проверяйте файл task21.csv')
