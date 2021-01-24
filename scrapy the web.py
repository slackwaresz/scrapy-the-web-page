import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from time import sleep
from random import randint
import numpy as np

headers = dict()
headers[
    "User-Agent"
] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

titles = []
time = []

pages = np.arange(2700, 2800, 1)
for page in pages:
    url = "https://" + str(page)
    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    block_div = soup.find_all('li', class_ = 'filter_item')
    # sleep(randint(2, 10))
    print(page)
    for blockSection in block_div:
        name = blockSection.find('div' ,class_='name').text
        titles.append(name)
        # print(titles)

blocks = pd.DataFrame(
        {
            "block": titles,

        }
)

blocks.to_csv(r"blocks.csv", mode='a', index=False, header=True)