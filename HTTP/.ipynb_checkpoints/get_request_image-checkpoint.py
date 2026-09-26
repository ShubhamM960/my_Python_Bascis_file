import requests, bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text, "lxml")

img_lst = soup.select('img')
