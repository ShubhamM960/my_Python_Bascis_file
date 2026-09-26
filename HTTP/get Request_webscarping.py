import requests, bs4

res = requests.get('http://www.example.com')
#print(res.content)     #res.json    #res.text

soup = bs4.BeautifulSoup(res.text, 'html.parser') #'lxml'
#print(soup)
#.select() ==> return all the value of tag / id/ class  in a "list"
#print(soup.select('p'))
value_lst = soup.select('p')

for x in value_lst : 
    print(x.getText())

#===========================
import requests, bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text, 'html.parser') #'lxml'

value_lst = soup.select('.toctext')

for x in value_lst : 
    print(x.getText())
    
#=============================================================
import requests, bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text, "lxml")

img_lst = soup.select('img')

for x in img_lst:
    print(x['src'])