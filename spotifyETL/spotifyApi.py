import requests
import json
import spotifyETL.cfg as cfg
import spotifyETL.BD as BD
import time

# Obtein number of followers from spotify playlist
def getFollowersPro():
    # Get the playlist id from the config file
    print('hola')
    playlist_id = cfg.playlist_id
    requests.get('http://104.198.96.207:8000/index.html?Lambda-linea12')
    previousFollowers = getPreviousFollowers()
    print('previous')
    requests.get('http://104.198.96.207:8000/index.html?Lambda-linea14')
    # Get the token from the config file
    token = getToken()
    print('Token obtenido', token)
    # Get the playlist followers
    response = requests.get('https://api.spotify.com/v1/playlists/' + playlist_id, headers={"Authorization": "Bearer " + token['access_token']})
    print('Le pegue a spotify')
    # Convert the response to json
    json_data = json.loads(response.text)
    # Get the number of followers
    followers = json_data
    # Return the number of followers
    followers= followers['followers']['total']
    newFollowers = previousFollowers[3]
    unFollowers = previousFollowers[4]
    # Compare the number of followers with the previous number of followers
    if followers > previousFollowers[2]:
        newFollowers += followers - previousFollowers[2]
        # Save the newFollowers in the database
        requests.get('http://104.198.96.207:8000/index.html?Entre a followers > previousFollowers[2]')
        saveFollowers(previousFollowers[0],followers, newFollowers, unFollowers)
        
    elif followers < previousFollowers[2]:
        unFollowers += previousFollowers - followers
        saveFollowers(previousFollowers[0],followers, newFollowers, unFollowers)

    return followers, newFollowers, unFollowers

# Get token of Auth0 SpotifyWebAPi
def getToken():
    # Get the client_id from the config file
    client_id = cfg.client_id
    # Get the client_secret from the config file
    client_secret = cfg.client_secret
    # Get the token
    print('hola')
    response = requests.post('https://accounts.spotify.com/api/token', data={'grant_type': 'client_credentials'}, auth=(client_id, client_secret))
    # Convert the response to json
    json_data = json.loads(response.text)
    # Get the token
    token = json_data
    # Return the token
    return token

# Save the number of followers, newFollowers, unFollowers in the database
def saveFollowers(id, followers, newFollowers, unFollowers):
    # Connect to the database
    timeNow = time.strftime("%c")
    id+=1
    print(id, timeNow)
    conn = BD.connectToDatabase()
    cursor = conn.cursor()
    # run a query to update the number of follow[82186, 1186, 0]ers, newFollowers, unFollowers in the database   
    cursor.execute("INSERT INTO followers (id, lastUpdate, followers, newFollowers, unFollowers) VALUES (%s,%s,%s,%s,%s)", (id, timeNow, followers, newFollowers, unFollowers))
    try:
        conn.commit()
    except Exception as error:
        print('Hubo un error: ', error)
    # Close the connection
    requests.get('http://104.198.96.207:8000/index.html?guardefollowers')
    BD.dissconectFromDatabase(conn)
    print('Se guardo el numero de followers en la BD')

# Get the previous number of followers
def getPreviousFollowers():
    print('hola 2')
    conn = BD.connectToDatabase()
    cursor = conn.cursor()
    # run the query
    cursor.execute("SELECT * FROM followers ORDER BY id DESC LIMIT 1")
    # Get the result
    result = cursor.fetchone()
    # Close the connection
    BD.dissconectFromDatabase(conn)
    # Return the result
    return result 
