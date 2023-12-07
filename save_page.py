import re
import json
import os
import requests
import fake_useragent
from bs4 import BeautifulSoup


def save(link):

    userFake = fake_useragent.UserAgent().random
    header = {'userFake': userFake}
    html = requests.get(link, headers=header)
    bs = BeautifulSoup(html.text, 'html.parser')

    print(link, '<<<link')

    def saveName():
        value = str(bs.find('h1', {'itemprop': 'name'}).get_text())
        value = value.replace('\n', '')
        value = value.replace(' ', '')
        return value

    def savePrice():
        value = str(bs.find('div', {'id': 'results-price'}).get_text())
        return value
     
    def saveDescription():
        value = str(bs.find('div', {'class': 'mobile-tabler-content'}))
        return value

    def saveImage(name):
        # Сохранение фотографий
        os.mkdir(f'db_data/{name}/')
        listImage = []
        count = 1
        for img in bs.find_all('img', {'src': re.compile('.*400_400.*.jpg')}):
            if 'src' in img.attrs:
                image_save = requests.get(f"https://mirm.ru{img.attrs['src']}")
                print(name)
                out = open(f'db_data/{name}/{count}.jpg', 'wb')
                out.write(image_save.content)
                out.close()
                count += 1

        return listImage
   
    name = saveName()
    price = savePrice()
    description = saveDescription()
    print(name)
    saveImage(name)
    
    json_data = {
            'name': name,
            'price': price,
            'description': description
            }
    
    with open('db_json.json', 'a') as f:
        json.dump(json_data, f, sort_keys=True, indent=2)

    exit()
