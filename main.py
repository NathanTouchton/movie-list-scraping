from requests import get
from bs4 import BeautifulSoup

response = get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

news = soup.find_all(class_="titleline")
scores = soup.find_all(class_="score")

for headline in news:
    print(headline.find(name="a").getText())
    print(headline.find(name="a").get("href"))

for score in scores:
    print(int(score.getText().split(" ")[0]))
