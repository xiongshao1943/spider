from urllib import request
from lxml import etree

url = "https://movie.douban.com/top250?start={}&filter="
class DownLoadUrl():
    def __init__(self,url):
        self.url = url
        self.AllData(self.url)

    def AllData(self,url):
        response = request.urlopen(url).read()
        response.decode("utf-8")
        selector = etree.HTML(response)
        alldata = selector.xpath('//div[@class="info"]')
        self.Title(alldata)

    def Title(self,data):
        result = []
        key = {}
        for title in data:
            name = title.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
            othername = title.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
            desc = title.xpath('div[@class="bd"]/p/text()')
            star_1 = title.xpath('div[@class="bd"]/div[@class="star"]/span[1]/@class')
            star_2 = title.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
            star_3 = title.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')
            quote = title.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
            link = title.xpath('div[@class="hd"]/a/@href')
            key['name'] = ''.join(name + othername)
            key['desc'] = ''.join(desc).strip()
            key['star'] = ''.join(star_1) + ' ' + ''.join(star_2) + ' ' + ''.join(star_3)
            key['quote'] = ''.join(quote)
            key['link'] = ''.join(link)
            result.append(''.join(sorted(key.values())))
        self.WriteFile(result)

    def WriteFile(self,data):
        with open('DouBanUrl.txt','a+',encoding='utf-8') as f:
            for line in data:
                f.write(line)


if __name__ == '__main__':
    for i in range(0,10):
        DownLoadUrl(url.format(i * 25))