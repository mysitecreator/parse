import requests
from bs4 import BeautifulSoup as bs
import random

async def get_random_product():
    base_url = 'http://allbazar.uz'
    url = 'http://allbazar.uz/brand-nivea_i29609/'
    r = requests.get(url)

    soup = bs(r.content, features='html.parser')

    info = soup.find_all('div', class_='top-product--item')
    product_list = []

    for products in info:
        product = {}
        # print(f"{title} | {link}")
        product['image'] = base_url + products.find_next('div', class_='top-product--img-block').img['src']
        product['price'] = products.find_next('a', class_='top-product--price').text.strip()
        product['title'] = products.find_next('span', class_='top-product--price').text.strip()
        product['link'] = base_url + products.find_next('a', class_='top-product--price')['href']

        product_list.append(product)

    send_product = random.choice(product_list)

    return send_product



# base_url = 'http://allbazar.uz'
# url = 'http://allbazar.uz/'
# r = requests.get(url)
#
# soup = bs(r.text, features='html.parser')
#
# article_list = []
# for articles in soup.find_all('div', class_='top-product--item'):
#
#     info = soup.find('a', {"class": "top-product--price"})
#
#     article = {}
#
#     article['image'] = base_url + articles.find('div', class_='top-product--img-block').img['src']
#     article['title'] = soup.find('a', class_='top-product--price').text.strip()
#     # article['link'] = base_url + info['href']
#
#     # div = soup.find('div', {"class": "top-product--img-block"})
#     # img_src1 = div.find('img').attrs['src']
#     img_src = articles.find('div', class_='top-product--img-block').img['src']
#
#     # print(article_list.append(article))
#
#     # print(img_src1)
#     print(base_url + img_src)