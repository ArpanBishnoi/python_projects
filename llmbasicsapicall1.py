import requests
API_KEY = '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'
url = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': 'You are a helpful teacher'},
        {'role': 'user', 'content': 'Explain the use of Python 5 lines'}
    ] 
}
response = requests.post(url,headers=headers, json=data)
print(response.json())
fake