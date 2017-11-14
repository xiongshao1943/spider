from urllib import request
from lxml import etree
from selenium import webdriver

url = "https://movie.douban.com/chart"

response = request.urlopen(url)

data = response.read().decode('utf-8')

move_list = []
move_name = []

html = etree.HTML(data)

moves = html.xpath('//*[@id="content"]/div/div/div/div/table/tr/td[2]/div/a//text()')
for i in moves:
    move_list.append(i.strip().replace(' ',''))

print(len(move_list))
print(move_list)

#movename = html.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[1]/a/@href')
#for i in movename:
#    move_name.append(i.strip().replace(' ',''))
#print(len(movename))
#print(movename)