import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = "xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77"
client = WebClient(token=slack_token)
channel_id = "C090QB0L230"


response = requests.get('https://api.imgflip.com/get_memes')
with open('/Users/arsen2000/Documents/КШЕ/ОП/kse_new/seminar_11/meme.jpg', 'wb') as f:
    f.write(response.content)

file_path = "ОП/kse_new/seminar_11/meme.jpg"

try:
    response = client.files_upload_v2(
        channel=channel_id,
        file=file_path,
        filename="meme.jpg",
        title="Моє зображення",
        initial_comment=""
    )
    print("✅ Файл надіслано:", response["file"]["permalink"])
except SlackApiError as e:
    print("❌ Помилка при надсиланні:", e.response["error"])