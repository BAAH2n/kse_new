import requests

file_path = 'ОП/kse_new/seminar_11/image.png'
slack_token = 'xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77'

with open(file_path, "rb") as file_content:
    response = requests.post(
        "https://slack.com/api/files.upload",
        headers={
            "Authorization": f"Bearer {slack_token}"
        },
        files={
            "file": file_content
        },
        data={
            "channels": 'C090QB0L230',
            "filename": "photo.jpg",
            "initial_comment": "Стадний",
            "title": "Стадний"
        }
    )
if response.ok and response.json().get("ok"):
    print("Повідомлення надіслано успішно")
else:
    print("Помилка при надсиланні:", response.text)