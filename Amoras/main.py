from tkinter import *
import requests
def pegar_cotacao():
    requisita= requests.get("http://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    RQS=requisita.jon()
    dola_atual= rqs['USDBRL']['bid']
    euro_atual=rqs['EURBRL']['bid']
    bitcoin_atual=rqs [BTCBRL]['bid']
    
    texto=f'''
    dola:{dola_atual}
    euro:{euro_atual}
    btc:{bitcoin_atual}'''
    print(texto)
pegar_cotacao()
