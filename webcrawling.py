from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

url = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%98%A4%EB%8A%98%EB%82%A0%EC%94%A8&oquery=&tqi=hMILRwprvhGssKWXWy8ssssstqV-287229&acq=dhsmfskfTl&acr=1&qdt=0'
html = req.get(url)
#pprint(html.text)
soup = bs(html.text, 'html.parser')

finedust = soup.find('div', {'class': 'detail_box'})
#pprint(finedust)
details = finedust.findAll('dd')
#print(details)


#미세먼지
finedust = details[0].find('span', {'class', 'num'}).get_text()
pprint(finedust)
#초미세먼지
ultrafinedust = details[1].find('span', {'class', 'num'}).get_text()
#오존지수 

ozone = details[2].find('span', {'class', 'num'}).get_text()

print('{0}, {1}, {2}'.format(finedust, ultrafinedust, ozone))