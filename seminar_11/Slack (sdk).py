from slack_sdk import WebClient

slack_token = "xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77"
client = WebClient(token=slack_token)


channel_id = "C090QB0L230" 


response = client.chat_postMessage(
    channel=channel_id,
    text="Пупупу"
)