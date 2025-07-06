import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.gutenberg.org/ebooks/bookshelf/443"  # прикладна сторінка
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Збираємо всі блоки книжок
books = soup.find_all("li", class_="booklink")

data = []
for book in books:
    title_tag = book.find("span", class_="title")
    subtitle_tag = book.find("span", class_="subtitle")
    extra_tag = book.find("span", class_="extra")

    title = title_tag.get_text(strip=True) if title_tag else "—"
    subtitle = subtitle_tag.get_text(strip=True) if subtitle_tag else "—"
    extra = extra_tag.get_text(strip=True) if extra_tag else "—"

    data.append({
        "Назва": title,
        "Автор": subtitle,
        "Опис/Інфо": extra
    })

# Створюємо DataFrame
df = pd.DataFrame(data)

# Показуємо перші 5 рядків
print(df.to_string(index=False))
