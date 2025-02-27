#https://store.steampowered.com/specials
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

import logging

import time


from utils.extract import extract_full_body_from
from utils.parse import  parse_raw_attributes
from utils.process import format_and_transform,save_to_file
from config.tools import get_config



#https://playwright.dev/python/docs/
#dependencies= pip install playwright selectolax
#playwright install


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
#logging.info(f'Downloading {url}...')








# URL = "https://store.steampowered.com/specials"
#https://store.steampowered.com/specials?offset=12

if __name__ == "__main__":
     config =get_config()
        
     html = extract_full_body_from(
             from_url=config.get('url'),
             wait_for=config.get('container').get('selector')
             )   #"div[class*='_2hhNOdcC6yLwL']"

     nodes=parse_raw_attributes(html,[config.get('container')])


     # tree = HTMLParser(html)
     #    # ImpressionTrackedElement
     # divs = tree.css(config.get('container').get('selector'))
     # print(len(divs))
     #    # print(divs)


     game_data = []
     for node in nodes.get("store_sale_divs"):
                
            attrs =parse_raw_attributes(node,config.get('item'))
            attrs =format_and_transform(attrs)
            game_data.append(attrs)

     # print(game_data)
     save_to_file('extract',game_data)











# ---------------------------Initial Code----------------------------------------------------
            # title = d.css_first("div[class*='StoreSaleWidgetTitle']").text()
            
            # original_price=d.css_first("div[class*='_3fFFsvII7Y2KXNLDk_krOW']")
            # sale_price=d.css_first("div[class*='_3j4dI1yA7cRfCvK8h406OB']").text()

            # thumbnail=d.css_first('div[class*="_2oW_y7Mm3ihf1XQ0C1VWhx CapsuleImageCtn"]  > img').attributes.get('src')
            # tags=[a.text() for a in d.css('div[class*="_2bkP-3b7dvr0a"] > a')[:5]]
            # release_date=d.css_first("div[class*='_1qvTFgmehUzbdYM9cw0eS7']").text()
            # review_score=d.css_first("div[class*='_2nuoOi5kC2aUI12z85PneA']").text()
            # reviews=d.css_first("div[class*='_1wXL_MfRpdKQ3wZiNP5lrH']").text().split(" ")[0]

            # if attrs['original_price'] is not None:
            #     attrs['original_price'] = attrs['original_price']
            # else:
            #     attrs['original_price']='NAN'

            # # original_price=[lambda original_price: original_price.text() is not None]
            
            # attrs={
            #     'title':title,
            #     'sale_price':sale_price,
            #     'original_price':original_price,
            #     'tags':tags,
            #     'release_data':release_date,
            #     'review_score':review_score,
            #     'reviews':reviews,
            #     'thumbnail':thumbnail,
                
            # }

            


# _3NhLu7mTdty7JufpSpz6Re

#_2s-O5T3qJJYR2AUq4b9jIN StoreSalePriceWidgetContainer _1g0B-RjwkUV0_MDURgy3Bi Discounted



   


    

