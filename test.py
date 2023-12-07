import re
import requests
import fake_useragent
from bs4 import BeautifulSoup



userFake = fake_useragent.UserAgent().random
header = {'userFake': userFake}
html = requests.get('https://mirm.ru/catalog/products/nektar_impact_gxp88', headers=header)
bs = BeautifulSoup(html.text, 'html.parser')


# value = bs.find_all('a', {'href': '/info/img_1200/CNT95432.jpg'})
value = bs.find_all('img', {'src': re.compile('.*400_400.*.jpg')})
count = 1
for v in value:
    if 'src' in v.attrs:
        print(f"https://mirm.ru{v.attrs['src']}")
        image_save = requests.get(f"https://mirm.ru{v.attrs['src']}")
        out = open(f'{count}.jpg', "wb")
        out.write(image_save.content)
        out.close()
        count += 1
# value = bs.find_all('a')
