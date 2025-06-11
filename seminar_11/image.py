from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = "xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77"
client = WebClient(token=slack_token)
channel_id = "C090QB0L230"
file_path = "ОП/kse_new/seminar_11/image.png"

try:
    response = client.files_upload_v2(
        channel=channel_id,
        file=file_path,
        filename="photo.jpg",
        title="Моє зображення",
        initial_comment="Стадний 😊"
    )
    print("✅ Файл надіслано:", response["file"]["permalink"])
except SlackApiError as e:
    print("❌ Помилка при надсиланні:", e.response["error"])
