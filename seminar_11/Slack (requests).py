import requests

response = requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77", "Content-Type": "application/json"}, json={"channel": "C090QB0L230", "text": "Повідомлення від Єрмака: 'Зайдіть до мене, негайно!"})
if response.ok and response.json().get("ok"):
    print("Повідомлення надіслано успішно")
else:
    print("Помилка при надсиланні:", response.text)