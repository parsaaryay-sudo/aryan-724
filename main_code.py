import requests
import time
from cachetools import cached , TTLCache

@cached(TTLCache(maxsize=200 , ttl=10*60))
def rate_changer(base_currency , target_currency) :
    
    url = f'https://v6.exchangerate-api.com/v6/d44b27a7974b374440074114/latest/{base_currency}'
    params = {'api_key' : 'd44b27a7974b374440074114'}
    data = requests.get(url , params=params) 

    return data.json()['conversion_rates'][target_currency]

def convert_currency(amount , exchange_rate) :
    return amount * exchange_rate

