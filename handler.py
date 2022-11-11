from requests import get
from spotifyETL import spotifyApi
import json

def followers(event, context):
    print('followers handler')
    response = spotifyApi.getFollowersPro()
    return {"statusCode": 200, "body": json.dumps(response)}
