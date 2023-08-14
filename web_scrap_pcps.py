import requests
from bs4 import BeautifulSoup

url = "https://patancollege.edu.np/our-courses/"

def get_content(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    # print(soup)

    paragraph = soup.find_all("p", class_= "sub-title")
    # print(paragraph)

    course_names = []  # Create a list to store course names

    for p in paragraph:
        course_link = p.find("a")  # Find the <a> tag within the <p> tag
        course_name = course_link.get_text()  # Get the text within the <a> tag
        course_names.append(course_name)  # Add the course name to the list

    # return course_names  # Return the list of course names
    
    for course in course_names:
        # print (f"Course Name : {course}")
        print(course)



    # content = paragraph.find_all(class_='sub-title subtitle-selector')
   

if __name__ == '__main__':
    get_content(url)
