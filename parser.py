from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import save_page

options = Options()
options.headless = True
# Запуск хрома
driver = webdriver.Firefox(options=options)

# Список ссылок
link_list = [
        'https://mirm.ru/catalog/klavishnie-inctrumenti/cifrovie-fortepiano-i-organi/',
        'https://mirm.ru/catalog/klavishnie-inctrumenti/cintezatori/',
        'https://mirm.ru/catalog/klavishnie-inctrumenti/midi-klaviaturi/',
        'https://mirm.ru/catalog/klavishnie-inctrumenti/akucticheckie-klavishnie/',
        'https://mirm.ru/catalog/klavishnie-inctrumenti/akceccuari-k-klavishnim-inctrumentam/'
        ]

# Загрузка погинатора
def scroll_page_paginator():
    list_link_run = set()
    list_link_run.add(driver.current_url)
    list_link = driver.find_elements(By.XPATH, "//ul[@class='pagination pull-left']/li/a")
    for link in list_link:
        list_link_run.add(link.get_attribute('href'))

    return list_link_run

count = 0
# прохожу по ссылкам из списка
for link in link_list:
    driver.get(link)
    sleep(2)
    list_paginator = scroll_page_paginator()

    # проходит по погинатору
    xpath = "//div[@class='showcase-list']//div[@class='showcase-name']/a"
    for paginator in list_paginator:
        driver.get(paginator)
        sleep(2)
        # Находим на странице все ссылки пагинатора и передаем в save_page.save()
        for page in driver.find_elements(By.XPATH, xpath):
            sleep(2)
            # Передаем ссылку и получаем все данные из карты товара
            save_page.save(str(page.get_attribute('href')))
    
driver.quit()

