import requests


responce = requests.get(url='https://vk.com/im?peers=407588953_661431633&sel=85900686')

with open('uhan_on.txt', mode='w', encoding='utf8') as on:
    on.write(responce.text)
