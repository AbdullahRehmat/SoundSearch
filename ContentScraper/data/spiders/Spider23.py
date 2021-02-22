from scrapy import Spider
from scrapy.selector import Selector
from data.items import DataItem


class SpiderTwentyThree(Spider):
    name = "data"

    allowed_domains = [
        "www.salafisounds.com"
    ]

    start_urls = [
        "https://www.salafisounds.com/category/speakers/",
        "https://www.salafisounds.com/category/speakers/page/2/",
        "https://www.salafisounds.com/category/speakers/page/3/",
        "https://www.salafisounds.com/category/speakers/page/4/",
        "https://www.salafisounds.com/category/speakers/page/5/",
        "https://www.salafisounds.com/category/speakers/page/6/",
        "https://www.salafisounds.com/category/speakers/page/7/",
        "https://www.salafisounds.com/category/speakers/page/8/",
        "https://www.salafisounds.com/category/speakers/page/9/",
        "https://www.salafisounds.com/category/speakers/page/10/",
        "https://www.salafisounds.com/category/speakers/page/11/",
        "https://www.salafisounds.com/category/speakers/page/12/",
        "https://www.salafisounds.com/category/speakers/page/13/",
        "https://www.salafisounds.com/category/speakers/page/14/",
        "https://www.salafisounds.com/category/speakers/page/15/",
        "https://www.salafisounds.com/category/speakers/page/16/",
        "https://www.salafisounds.com/category/speakers/page/17/",
        "https://www.salafisounds.com/category/speakers/page/18/",
        "https://www.salafisounds.com/category/speakers/page/19/",
        "https://www.salafisounds.com/category/speakers/page/20/",
        "https://www.salafisounds.com/category/speakers/page/21/",
        "https://www.salafisounds.com/category/speakers/page/22/",
        "https://www.salafisounds.com/category/speakers/page/23/",
        "https://www.salafisounds.com/category/speakers/page/24/",
        "https://www.salafisounds.com/category/speakers/page/25/",
        "https://www.salafisounds.com/category/speakers/page/26/",
        "https://www.salafisounds.com/category/speakers/page/27/",
        "https://www.salafisounds.com/category/speakers/page/28/",
        "https://www.salafisounds.com/category/speakers/page/29/",
        "https://www.salafisounds.com/category/speakers/page/30/",
        "https://www.salafisounds.com/category/speakers/page/31/",
        "https://www.salafisounds.com/category/speakers/page/32/",
        "https://www.salafisounds.com/category/speakers/page/33/",
        "https://www.salafisounds.com/category/speakers/page/34/",
        "https://www.salafisounds.com/category/speakers/page/35/",
        "https://www.salafisounds.com/category/speakers/page/36/",
        "https://www.salafisounds.com/category/speakers/page/37/",
        "https://www.salafisounds.com/category/speakers/page/38/",
        "https://www.salafisounds.com/category/speakers/page/39/",
        "https://www.salafisounds.com/category/speakers/page/40/",
        "https://www.salafisounds.com/category/speakers/page/41/",
        "https://www.salafisounds.com/category/speakers/page/42/",
        "https://www.salafisounds.com/category/speakers/page/43/",
        "https://www.salafisounds.com/category/speakers/page/44/",
        "https://www.salafisounds.com/category/speakers/page/45/",
        "https://www.salafisounds.com/category/speakers/page/46/",
        "https://www.salafisounds.com/category/speakers/page/47/",
        "https://www.salafisounds.com/category/speakers/page/48/",
        "https://www.salafisounds.com/category/speakers/page/49/",
        "https://www.salafisounds.com/category/speakers/page/50/",
        "https://www.salafisounds.com/category/speakers/page/51/",
        "https://www.salafisounds.com/category/speakers/page/52/",
        "https://www.salafisounds.com/category/speakers/page/53/",
        "https://www.salafisounds.com/category/speakers/page/54/",
        "https://www.salafisounds.com/category/speakers/page/55/",
        "https://www.salafisounds.com/category/speakers/page/56/",
        "https://www.salafisounds.com/category/speakers/page/57/",
        "https://www.salafisounds.com/category/speakers/page/58/",
        "https://www.salafisounds.com/category/speakers/page/59/",
        "https://www.salafisounds.com/category/speakers/page/60/",
        "https://www.salafisounds.com/category/speakers/page/61/",
        "https://www.salafisounds.com/category/speakers/page/62/",
        "https://www.salafisounds.com/category/speakers/page/63/",
        "https://www.salafisounds.com/category/speakers/page/64/",
        "https://www.salafisounds.com/category/speakers/page/65/",
        "https://www.salafisounds.com/category/speakers/page/66/",
        "https://www.salafisounds.com/category/speakers/page/67/",
        "https://www.salafisounds.com/category/speakers/page/68/",
        "https://www.salafisounds.com/category/speakers/page/69/",
        "https://www.salafisounds.com/category/speakers/page/70/",
        "https://www.salafisounds.com/category/speakers/page/71/",
        "https://www.salafisounds.com/category/speakers/page/72/",
        "https://www.salafisounds.com/category/speakers/page/73/",
        "https://www.salafisounds.com/category/speakers/page/74/",
        "https://www.salafisounds.com/category/speakers/page/75/",
        "https://www.salafisounds.com/category/speakers/page/76/",
        "https://www.salafisounds.com/category/speakers/page/77/",
        "https://www.salafisounds.com/category/speakers/page/78/",
        "https://www.salafisounds.com/category/speakers/page/79/",
        "https://www.salafisounds.com/category/speakers/page/80/",
        "https://www.salafisounds.com/category/speakers/page/90/",
        "https://www.salafisounds.com/category/speakers/page/91/",
        "https://www.salafisounds.com/category/speakers/page/92/",
        "https://www.salafisounds.com/category/speakers/page/93/",
        "https://www.salafisounds.com/category/speakers/page/94/",
        "https://www.salafisounds.com/category/speakers/page/95/",
        "https://www.salafisounds.com/category/speakers/page/96/",
        "https://www.salafisounds.com/category/speakers/page/97/",
        "https://www.salafisounds.com/category/speakers/page/98/",
        "https://www.salafisounds.com/category/speakers/page/99/",
        "https://www.salafisounds.com/category/speakers/page/100/",
        "https://www.salafisounds.com/category/speakers/page/101/",
        "https://www.salafisounds.com/category/speakers/page/102/",
        "https://www.salafisounds.com/category/speakers/page/103/",
        "https://www.salafisounds.com/category/speakers/page/104/",
        "https://www.salafisounds.com/category/speakers/page/105/",
        "https://www.salafisounds.com/category/speakers/page/106/",
        "https://www.salafisounds.com/category/speakers/page/107/",
        "https://www.salafisounds.com/category/speakers/page/108/",
        "https://www.salafisounds.com/category/speakers/page/109/",
        "https://www.salafisounds.com/category/speakers/page/110/",
        "https://www.salafisounds.com/category/speakers/page/111/",
        "https://www.salafisounds.com/category/speakers/page/112/",
        "https://www.salafisounds.com/category/speakers/page/113/",
        "https://www.salafisounds.com/category/speakers/page/114/",
        "https://www.salafisounds.com/category/speakers/page/115/",
        "https://www.salafisounds.com/category/speakers/page/116/",
        "https://www.salafisounds.com/category/speakers/page/117/",
        "https://www.salafisounds.com/category/speakers/page/118/",
        "https://www.salafisounds.com/category/speakers/page/119/",
        "https://www.salafisounds.com/category/speakers/page/120/",
        "https://www.salafisounds.com/category/speakers/page/121/",
        "https://www.salafisounds.com/category/speakers/page/122/",
        "https://www.salafisounds.com/category/speakers/page/123/",
        "https://www.salafisounds.com/category/speakers/page/124/",
        "https://www.salafisounds.com/category/speakers/page/125/",
        "https://www.salafisounds.com/category/speakers/page/126/",
        "https://www.salafisounds.com/category/speakers/page/127/",
        "https://www.salafisounds.com/category/speakers/page/128/",
        "https://www.salafisounds.com/category/speakers/page/129/",
        "https://www.salafisounds.com/category/speakers/page/130/",
        "https://www.salafisounds.com/category/speakers/page/131/",
        "https://www.salafisounds.com/category/speakers/page/132/",
        "https://www.salafisounds.com/category/speakers/page/133/",
        "https://www.salafisounds.com/category/speakers/page/134/",
        "https://www.salafisounds.com/category/speakers/page/135/",
        "https://www.salafisounds.com/category/speakers/page/136/",
        "https://www.salafisounds.com/category/speakers/page/137/",
        "https://www.salafisounds.com/category/speakers/page/138/",
        "https://www.salafisounds.com/category/speakers/page/139/",
        "https://www.salafisounds.com/category/speakers/page/130/",
        "https://www.salafisounds.com/category/speakers/page/131/",
        "https://www.salafisounds.com/category/speakers/page/132/",
        "https://www.salafisounds.com/category/speakers/page/133/",
        "https://www.salafisounds.com/category/speakers/page/134/",
        "https://www.salafisounds.com/category/speakers/page/135/",
        "https://www.salafisounds.com/category/speakers/page/136/",
        "https://www.salafisounds.com/category/speakers/page/137/",
        "https://www.salafisounds.com/category/speakers/page/138/",
        "https://www.salafisounds.com/category/speakers/page/139/",
        "https://www.salafisounds.com/category/speakers/page/140/",
        "https://www.salafisounds.com/category/speakers/page/141/",
        "https://www.salafisounds.com/category/speakers/page/142/",
        "https://www.salafisounds.com/category/speakers/page/143/", # <<-- 1269 Timeout Starts Here
        "https://www.salafisounds.com/category/speakers/page/144/",
        "https://www.salafisounds.com/category/speakers/page/145/",
        "https://www.salafisounds.com/category/speakers/page/146/",
        "https://www.salafisounds.com/category/speakers/page/147/",
        "https://www.salafisounds.com/category/speakers/page/148/",
        "https://www.salafisounds.com/category/speakers/page/149/",
        "https://www.salafisounds.com/category/speakers/page/150/",
        "https://www.salafisounds.com/category/speakers/page/151/",
        "https://www.salafisounds.com/category/speakers/page/152/",
        "https://www.salafisounds.com/category/speakers/page/153/",
        "https://www.salafisounds.com/category/speakers/page/153/",
        "https://www.salafisounds.com/category/speakers/page/154/",
        "https://www.salafisounds.com/category/speakers/page/155/",
        "https://www.salafisounds.com/category/speakers/page/156/",
        "https://www.salafisounds.com/category/speakers/page/157/",
        "https://www.salafisounds.com/category/speakers/page/158/",
        "https://www.salafisounds.com/category/speakers/page/159/",
        "https://www.salafisounds.com/category/speakers/page/160/",
        "https://www.salafisounds.com/category/speakers/page/161/",
        "https://www.salafisounds.com/category/speakers/page/162/",
        "https://www.salafisounds.com/category/speakers/page/163/",
        "https://www.salafisounds.com/category/speakers/page/164/",
    ]

    def parse(self, response):
        scrapedData = Selector(response).css('h3.mh-posts-list-title')

        for data in scrapedData:
            item = DataItem()
            #item['title'] = data.css('h3.mh-posts-list-title > a::text').get(),
            item['title'] = data.css('h3.mh-posts-list-title > a::attr(title)').get(),
            item['source'] = 'Salafi Sounds - Audio',
            item['url'] = data.css('h3.mh-posts-list-title > a::attr(href)').get()
            yield item