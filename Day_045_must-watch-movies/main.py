import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
internet_archives_empire_top100 = response.text

# ref
# <h3 class="title">100) Stand By Me</h3>

soup = BeautifulSoup(internet_archives_empire_top100, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

movie_list = [m.getText() for m in movie_titles]
movie_list = movie_list[::-1]

movies_text = ""
for m in movie_list:
    movies_text += f"{m}\n"


print(movie_list)
print(movies_text)
