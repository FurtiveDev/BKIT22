import requests
from datetime import datetime


def get_data(text):
    try:
        req = requests.get(f"https://yobit.net/api/3/ticker/{text}")
        response = req.json()
        print(req)
        sell_price = response[f'{text}']["sell"]
        return(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nSell {text} price: {sell_price}")
    except:
        return None
