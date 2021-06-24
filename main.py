import requests


# ________________________P.O.S.T______________________

url = 'http://192.168.64.3:8000/product/'

product_data_post = {
    "name": "produto1",
    "description": "teste1",
    "price": 1000.0,
    "category": 1
}
response = requests.post(url=url, json=product_data_post)

# ________________________G.E.T_________________________

# url = 'http://192.168.64.3:8000/product/1'

# response = requests.get(url=url)

#________________________________________________________

print('\n','='*40, 'Imprimindo requisições', '='*40 ,'\n')

if response.status_code >= 200 and response.status_code <= 299:
    print('Status code', response.status_code)
    print('Reason', response.text)
    print('Texto', response.content)
    print('JSON', response.json())

else:
    print('Status code', response.status_code)
    print('Reason', response.text)
    print('Texto', response.content)