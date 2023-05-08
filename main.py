from requests import get
from bs4 import BeautifulSoup

response = get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# news = soup.find(class_="titleline")

# for headline in news:
#     soup.find(name="a").get()

print(soup.find(class_="titleline"))
