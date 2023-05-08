# from pprint import pprint
from requests import get
from bs4 import BeautifulSoup

response = get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("main .title")
titles_list = []
for item in titles:
    text = item.get_text()
    titles_list.insert(0, text)

with open("list.txt", "w+") as file:
    for movie in titles_list:
        file.write(movie + "\n")
