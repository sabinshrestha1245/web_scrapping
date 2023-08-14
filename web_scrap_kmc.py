import requests
from bs4 import BeautifulSoup

url = "https://ktmmodelcollege.edu.np/"

def get_content(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html5lib')
    courses = soup.find_all("div", class_="gdlr-core-tab-item-wrap")
    # courses = soup.find()
    print(courses)
    # lists=[]

    # for ul in courses:
    #     list = ul.find("ul")
    #     list_name = list.get_text()
    #     lists.append(list_name)

    # print(lists)

if __name__ == '__main__':
    get_content(url)