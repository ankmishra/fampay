from celery.decorators import task
import requests
import datetime
from .models import Video

@task(name="fetch_latest_videos")
def fetch_latest_videos():
    d = datetime.datetime.utcnow()
    dt = d - datetime.timedelta(seconds = 60)
    dt = dt.isoformat("T") + "Z"
    payload = {'part':'snippet', 
        'type': 'video', 
        'key': 'AIzaSyCqVFqungxvH9HyJq35w3VpVhm6lNVRQDo',
        'q': 'cricket', 
        'order': 'date', 
        'publishedAfter': dt
    }
    url = 'https://www.googleapis.com/youtube/v3/search'
    r = requests.get(url, params=payload)
    if r.status_code == 200:
        response = r.json()
        for item in response['items']:
            Video.objects.create(title=item['snippet']['title'], 
                                description=item['snippet']['description'],
                                published_at=item['snippet']['publishedAt'],
                                thumbnail_url=item['snippet']['thumbnails']['default']['url'],
                                )
    return True