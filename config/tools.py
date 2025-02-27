import json



_config={

    'url':"https://store.steampowered.com/specials",
    'meta':
    {
        'name':"Steam sales scraper",
        'description':'Extracts the highest discounted games from Steam',
        'author':'Nomad Coder',
        'version':'0.1'

    },
    'container':
        {
            'name':'store_sale_divs',
            'selector':"div[class*='_2hhNOdcC6yLwL']",
            'match':'all',
            'type':'node'
            

        }
    ,
    'item':[
        {
            'name':'title',
            'selector':"div[class*='StoreSaleWidgetTitle']",
            'match':'first',
            'type':'text'

        },
            {
            'name':'original_price',
            'selector':"div[class*='_3fFFsvII7Y2KXNLDk_krOW']",
            'match':'first',
            'type':'node'

        },
            {
            'name':'sale_price',
            'selector':"div[class*='_3j4dI1yA7cRfCvK8h406OB']",
            'match':'first',
            'type':'node' 

        },
                    {
            'name':'price_currency',
            'selector':"div[class*='_3j4dI1yA7cRfCvK8h406OB']",
            'match':'first',
            'type':'node' 

        },
           
                    {
            'name':'thumbnail',
            'selector':'div[class*="_2oW_y7Mm3ihf1XQ0C1VWhx CapsuleImageCtn"]  > img',
            'match':'first',
            'type':'node' 

        },
                {
            'name':'release_date',
            'selector':"div[class*='_1qvTFgmehUzbdYM9cw0eS7']",
            'match':'first',
            'type':'text' 

        },
              {
            'name':'review_score',
            'selector':"div[class*='_2nuoOi5kC2aUI12z85PneA']",
            'match':'first',
            'type':'text' 

        },
              {
            'name':'reviews',
            'selector':"div[class*='_1wXL_MfRpdKQ3wZiNP5lrH']",
            'match':'first',
            'type':'text' 

        },
             {
            'name':'tags',
            'selector':'div[class*="_2bkP-3b7dvr0a"] > a',
            'match':'all',
            'type':'text' 

        },
    ],
}


        
            # tags=[a.text() for a in d.css('div[class*="_2bkP-3b7dvr0a"] > a')[:5]]
           
            # review_score=d.css_first().text()
            # =d.css_first("div[class*='_1wXL_MfRpdKQ3wZiNP5lrH']").text().split(" ")[0]


def get_config(load_from_file=False):
    if load_from_file:
        with open('config.json','r') as f:
           return json.load(f)
    return _config



def generate_config():
    with open('config.json' ,'w') as f:
        json.dump(_config,f,indent=4)



if __name__ == "__main__":

    generate_config()
     