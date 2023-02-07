import requests
import re

result = requests.get('https://greenatom.ru/', 
                       headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
print(len(re.findall("<\w", result.text)), len(re.findall("<\w+\s+\w+=", result.text)))