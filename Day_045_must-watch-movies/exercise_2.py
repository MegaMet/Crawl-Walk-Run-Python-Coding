import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.siliconera.com/")
siliconera_homepage = response.text

soup = BeautifulSoup(siliconera_homepage, "html.parser")
articles = soup.find_all(class_="wp-block-gamurs-article-tile__link")
print(len(articles))
# [n for n in list_of_num if n%2 == 0]

# review_articles = []
# for a in articles:
#     article_title = a.find(class_="wp-block-gamurs-article-tile__content-article-info-title")
#     if "Review" in article_title.getText():
#         review_articles.append(a)
#         print(article_title.getText())

review_articles = [a for a in articles if "Review" in a.find(class_="wp-block-gamurs-article-tile__content-article-info-title").getText()]

for a in review_articles:
    review_score = int((a.find(name="span" , class_="tile-badge-text").getText()).replace(" ", ""))
    article_title = a.find(class_="wp-block-gamurs-article-tile__content-article-info-title")
    article_link = a.get('href')
    print(f"{article_title.getText()}\nfinal score: {review_score}/10\n{article_link}")
    # print(review_articles.index(a))



# review_articles = [a for a in articles if "Review" in a.find(class_="wp-block-gamurs-article-tile__content-article-info-title")]

# class_="wp-block-gamurs-article-tile__content-article-info-title"
# <a class="wp-block-gamurs-article-tile__link  " href="https://www.siliconera.com/review-quintessential-quintuplets-memories-of-a-quintessential-summer-has-a-packed-schedule/">