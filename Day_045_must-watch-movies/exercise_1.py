from bs4 import BeautifulSoup

with open ("website.html", encoding= "utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_a_tags = soup.find_all(name="a")
print(all_a_tags)

for tag in all_a_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find_all(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one(selector="#name")
print(name)

headings = soup.select_one(".heading")
print(headings)