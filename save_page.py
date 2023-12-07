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
        value = bs.find('h1', {'itemprop': 'name'}).get_text()
        return value

    def savePrice():
        value = bs.find('div', {'id': 'results-price'}).get_text()
        return value
     
    def saveDescription():
        value = bs.find('div', {'class': 'mobile-tabler-content'})
        return value
    
    def saveCharacteristic():
        value = bs.find('div', {'class': 'tabler-slick slick-initialized slick-slider'})
        print(value, '<<<')
        exit()
        return value
  

    def saveImage():
        listImage = []
        count = 1
        for img in bs.find_all('img', {'src': re.compile('.*400_400.*.jpg')}):
            if 'src' in img.attrs:
                print(f"https://mirm.ru{img.attrs['src']}")
                image_save = requests.get(f"https://mirm.ru{img.attrs['src']}")
                out = open(f'{count}.jpg', "wb")
                out.write(image_save.content)
                out.close()
                count += 1

        return listImage
   
    name = saveName()
    price = savePrice()
    description = saveDescription()
    image = saveImage()
    
    # # Сохранение фотографий
    os.mkdir(f'db_data/{name}/')
     
    num_name = 0
    for i in image:
        image_save = requests.get(i)
        out = open(f'db_data/{name}-{key}/name_{num_name}.jpg', "wb")
        out.write(image_save.content)
        out.close()
        sleep(2)
        num_name += 1
    
    json_data = {
            'description': description,
            'characteristic': characteristic,
            'name': name,
            'price': price
            }
    
    with open('db_json.json', 'a') as f:
        json.dump(json_data, f, sort_keys=true, indent=2)
