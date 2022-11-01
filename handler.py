from requests import get
import spotifyApi

def hello(event, context):
    response = get("https://dev.to/articles?tag=python")
    return {"statusCode": 200, "body": response.text}

def followers(event, context):
    response = get(spotifyApi.getFollowers())
    return {"statusCode": 200, "body": response.text}

def previousFollowers(event, context):
    response = get(spotifyApi.getPreviousFollowers())
    return {"statusCode": 200, "body": response.text}   

    