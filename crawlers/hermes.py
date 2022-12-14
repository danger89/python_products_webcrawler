import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def set_header_user_agent():
    user_agent = UserAgent()
    return user_agent.random

def collect_product(url):
    user_agent = set_header_user_agent()
    print(f"collect_product,agent: {user_agent}")
    response = requests.get(url, headers={'user-agent': user_agent})

    soup = BeautifulSoup(response.content, 'html5lib')

    items = soup.findAll('div', attrs={'class': "product-item-meta"})

    products = []

    for item in items:
        # print(item.prettify())
        product_meta = {}
        try:
            product_meta["code"] = item['id']
            product_desc = " ".join(item.text.split())
            product_meta["description"] = product_desc

            products.append(product_meta)
        except TypeError as tex:
            print(f'collect_product, type error:{str(tex)}')
            continue
        except Exception as ex:
            print(f'collect_product, error:{str(ex)}')
            continue

    print(f"collect_product, product counts: {len(products)}")

    return products
