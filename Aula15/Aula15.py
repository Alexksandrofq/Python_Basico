import requests
import json
import time
import datetime

while True: 
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/:moedas')

    cotacao = json.loads(requisicao.text)

    print('#cotação#', datetime.datetimenow)
    print(cotacao['valores'] ['USD'] ['valor'])
    time.sleep(2)

