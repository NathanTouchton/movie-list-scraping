from bs4 import BeautifulSoup

with open("index.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
a = soup.find_all(name="a")

# for anchor in a:
#     print(anchor.get("href"))

company_website = soup.select_one("p a")

print(soup.select("#name"))
