import scrapy
from stockPriceFetcher.items import StockpricefetcherItem
import ipdb
import json

 # debugger
 # ipdb.set_trace()


class TeslaSpider (scrapy.Spider):
     name = "tesla"

     def start_requests(self):
         urls = [
              'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TSLA&apikey=27YYKZKYMR4W4MB0'
         ]

         for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

     def parse(self, response):
          #  WRITE THE RESPON TO A JSON FILE JUST BECAUSE
          # filename = "tesla_stockprice.json"

          # with open(filename, 'wb') as f:
          #      f.write(response.body)

          # SERIALIZE OBJECT FOR mongoDB 
          # for item in response:
          #      print(item)

          body = json.loads(response.body)

          for key, value in body['Monthly Time Series'].items():

               stockPrice = StockpricefetcherItem()
               stockPrice['date'] = key
               stockPrice['openPrice'] = value['1. open']
               stockPrice['highPrice'] = value['2. high']
               stockPrice['lowPrice'] = value['3. low']
               stockPrice['closePrice'] = value['4. close']
               stockPrice['volume'] = value['5. volume']

               # print(stockPrice, value)

               yield stockPrice


         



          