# {'title': 'DayZ',
#   'original_price': <Node div>,
#     'sale_price': '$24.99',
#       'price_currency': '$24.99',
#         'thumbnail': <Node img>,
#         'release_date': '', 
#         'review_score': 'Mostly Positive',
#         'reviews': '348,141 User Reviews', 
#         'tags': ['Survival', 'Open World', 'Online Co-Op', 'Zombies', 'Multiplayer', 'Post-apocalyptic', 'Shooter', 'PvP', 'Massively Multiplayer', 'Action', 'FPS', 'Horror', 'Co-op', 'Sandbox', 'Adventure', 'Survival Horror', 'Simulation', 'First-Person', 'Atmospheric', 'Choose Your Own Adventure']}



from  selectolax.parser import Node
from datetime import datetime
import re
import pandas  as pd

def get_attrs_from_node(node:Node,attr: str):
    if node is None or not issubclass(Node,type(node)):
        raise ValueError("The function expects a selectolax node to be provided.")

    return node.attributes.get(attr)

def get_text_if_not_none(node:Node,dowhat:str='currency'):
    if node is None or not issubclass(Node,type(node)):
        # raise ValueError("The function expects a selectolax node to be provided.")
        return "NAN"
    if dowhat =='currency':
        return node.text()[0]
    if dowhat == 'price':
    
        return  float(node.text()[1:])

def get_first_n(input_list:list,n:int=5):
    return input_list[:5]

def reformat_date(date_raw:str,input_format:str='%b %d, %Y', output_format:str='%Y-%m-%d'):
    if date_raw == '' :
        return "NAN"
    else:
        dt_obj = datetime.strptime(date_raw,input_format)
        # print(dt_obj)
    return datetime.strftime(dt_obj,output_format)


def regex(input_string:str,pattern:str,dowhat:str="findall"):
    if dowhat == 'findall':
        return re.findall(pattern,input_string)
    elif dowhat == 'split':
        return re.split(pattern,input_string)
    else:
        raise ValueError('The function expects findall or split to be provided')





def format_and_transform(attrs:dict):
    trasforms ={
        "thumbnail": lambda n: get_attrs_from_node(n,"src"),
        "original_price": lambda n: get_text_if_not_none(n,'price'),
        "tags":lambda input_list: get_first_n(input_list,5),
        "release_date":lambda date: reformat_date(date,'%b %d, %Y','%Y-%m-%d'),
        'reviews': lambda raw: int("".join(regex(raw,r'\d+','findall'))),
        'price_currency':lambda n: get_text_if_not_none(n,'currency'),
        'sale_price': lambda n: get_text_if_not_none(n,'price'),

    }

    for k,v in trasforms.items():
        if k in attrs:
            attrs[k]=v(attrs[k])

    attrs['discount_pct']=round(attrs['original_price'] - attrs['sale_price'] / attrs['original_price'] *100,3)
    
    return attrs



def save_to_file(filename:str='extract',data:list[dict]=None):

    if data is None:
        raise ValueError('Function expects data to be provided as list of dicts')
    
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename,index=False)
    
