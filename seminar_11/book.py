import requests

response = requests.get('https://www.gutenberg.org/ebooks/15776.txt.utf-8')
with open('/Users/arsen2000/Documents/КШЕ/ОП/kse_new/seminar_11/Book', 'w') as f:
    f.write(response.text)