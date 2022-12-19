import json
from pytube import YouTube
from collections import OrderedDict

def top_channles_watched(file):
    with open(file,encoding="utf8") as file:
        data=json.load(file)
    Userdata=dict()
    #c=1
    for item in data:
        try:
            video_url=item['titleUrl']
            channel_name=item["subtitles"][0]['name']
            if channel_name in Userdata.keys():
                Userdata[channel_name]+=1
            else:
                Userdata[channel_name]=1
        except Exception as e:
            pass
        #print(f"{c}/{len(data)}")
        #c+=1
    Userdata=OrderedDict(reversed(list(dict(sorted(Userdata.items(), key=lambda item: item[1])).items())))
    top_10=dict(zip(list(Userdata.keys())[:10], list(Userdata.values())[:10]))
    return top_10
    #add some mmore features
