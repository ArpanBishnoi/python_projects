import requests
response = requests.get('http://api.coincap.io/v2/assets/bitcoin')
data = response.json()
print('Bitcoin price(USD):',
data['data']['priceUSD'])
