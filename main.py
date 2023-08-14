# if you want to scrape a website:
# 1. use the api 
# 2. HTML web scraping using some tool bs4

# Step 0
# Requirements
# pip install requests
# pip install bs4
# pip install html5lib


import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"


# Step 1: Get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


# Step 3: HTML Tree traversal


# Get the title of the HTML page 
title = soup.title

# Commonly used types of objects:
# print(type(title))# 1. Tag
# print(type(title.string))# 2. NavigableString
# print(type(soup))# 3. BeautifulSoup
# 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))




# Get all the paragraphs from the page 
paras = soup.find_all('p')
# print(paras)

# Get all the anchor from the page 
# anchors = soup.find_all('a')
# print(anchors)


# Get first element in the HTML page
# print(soup.find('p'))

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements wtih class lead 
print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())

# Get all text from page
# print(soup.get_text())

# Get all the anchor from the page 
anchors = soup.find_all('a')

all_links = set()
# print(anchors)
# Get all the links on the page:
for link in anchors:
    if(link != '#'):
        linkText = "https://www.codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linkText)
        # print(all_links)