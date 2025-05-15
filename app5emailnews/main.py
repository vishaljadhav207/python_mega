import requests

url="https://epaper.lokmat.com/main-editions/Aurangabad%20Main/-1/1"
request=requests.get(url)
content=request.text
print(content)