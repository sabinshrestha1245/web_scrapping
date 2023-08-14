import requests
from bs4 import BeautifulSoup

url = "https://academy.united.edu.np/our-programs"

def get_content(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    courses = soup.find_all("h2", class_="text-3xl")

    # print(courses)

    for course in courses:
        print((course.text.strip()))

if __name__ == '__main__':
    get_content(url)
