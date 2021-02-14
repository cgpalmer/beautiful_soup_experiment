import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

page_url = "https://www.focusfinance.org/m-a-reports"

called_url = ureq(page_url)

page_html = called_url.read()

called_url.close()

page_soup = soup(page_html, "html.parser")

# Isolate the source of the iframe on the page
iframe = page_soup.findAll("iframe")
# print(iframe.attrs['src'])
print(iframe)





# # This will find all of the links from the iframe html
# links = page_soup.findAll("a")
# link_href = []
# for item in range(len(links)):
#     link_href.append(links[item].attrs['href'])

# link_href = list(dict.fromkeys(link_href))
# print(link_href)

