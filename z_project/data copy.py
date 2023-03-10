import requests
import string
from bs4 import BeautifulSoup

def preprocess(li):
    res = []
    new = ""
    for elem in li:
        new = elem.translate({ord(c): None for c in string.whitespace})
        lst = []
        temp = []
        for elem in new.split("<"):
            temp = elem.split(">")
            for factors in temp:
                lst.append(factors)
        # print(lst)
        for elem in lst:
            if elem != '':
                res.append(elem)
    for elem in res:
        print(elem)
    # print(res)

def parse(url):
    response = requests.get(url)
    new_str = ""
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        new_str = str(soup)
        # print(new_str)
        li = new_str.split("\n")
        preprocess(li)
    else : 
        print(response.status_code)
    
def main():
    url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
    parse(url)
    
if __name__ == main():
    main()