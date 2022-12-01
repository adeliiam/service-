import  requests
from bs4 import  BeautifulSoup as BS
import  json
import csv

url='https://roscarservis.ru/catalog/legkovye/'
req=requests.get(url)

with open('html_saita', 'w', encoding='utf-8') as file:
    file.write(req.text)
with open('html_saita',  encoding='utf-8') as file:
    html=file.read()
soup=BS(html, 'html.parser')

names_links=soup.findAll('a', class_='product__name')
namesLinksDict={}
for i in names_links:
    name=i.string
    link=i.get('href')
    namesLinksDict[name]=link
# вводим данные в формате json
with open('data_json.json','w', encoding='utf-8') as file:
    json.dump(namesLinksDict, file, indent=4, ensure_ascii=False)

# вводим данные в формате csv
with open('data_csv.csv', 'a', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(
        (
            'марка',
            'ссылка'
        )
    )
    for i in names_links:
        name = i.string
        link = i.get('href')
        writer.writerow(
            (name,
             link

            )
        )


