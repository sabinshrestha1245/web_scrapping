import requests
from bs4 import BeautifulSoup

url = "https://prasadi.edu.np/academic-programs/"

def get_content(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    cards = soup.find_all("div", class_="wpb_text_column vc_custom_1654669854671")

    # print(wrapper)
    course_names = []

    for card in cards:
        h3_elements = card.find_all("h3")
        for h3 in h3_elements:
            course_name = h3.get_text().strip()  # Get the text within the <a> tag
            course_names.append(course_name)  # Add the course name to the list
    return course_names

if __name__ == '__main__':
    courses = get_content(url)
    for course in courses:
        print(course + "\n")


