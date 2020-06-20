import requests
from lxml import html

search_term=input("Enter Search Term: ")
base_url = "https://www.dishtv.in/channelguide/search.aspx?q="
full_url=base_url+search_term
data = requests.get(full_url)

tree = html.fromstring(data.content)

showname = tree.xpath('//div[@class="sgrid"]//h4/text()')
genre_chname = tree.xpath('//div[@class="genre"]/text()')
images = tree.xpath('//div[@class="imgwrap"]//img/@src')
desc = tree.xpath('//div[@class="desc"]/text()')
timings = tree.xpath('//div[@class="timings"]/text()')
ch_number = tree.xpath('//div[@class="ch_number"]/text()')
print(showname)
print(len(showname))