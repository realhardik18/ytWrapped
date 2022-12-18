import json
from pytube import YouTube

with open('watch-history.json',encoding="utf8") as file:
    data=json.load(file)

Userdata=dict()

for item in data[:10]:
    video_url=item['titleUrl']
    channel_name=item["subtitles"][0]['name']
    video_lenght_seconds=YouTube(video_url).length
    if channel_name in Userdata.keys():
        Userdata[channel_name]+=video_lenght_seconds
    else:
        Userdata[channel_name]=video_lenght_seconds
print(Userdata)