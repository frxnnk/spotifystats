import requests
import json
import cfg
import BD
# Obtein number of followers from spotify playlist
def getFollowers():
    # Get the playlist id from the config file
    playlist_id = cfg.playlist_id
    # Get the token from the config file
    token = cfg.token
    # Get the playlist followers
    response = requests.get('https://api.spotify.com/v1/playlists/' + playlist_id, headers={"Authorization": "Bearer " + token})
    # Convert the response to json
    json_data = json.loads(response.text)
    # Get the number of followers
    followers = json_data['followers']['total']
    # Return the number of followers
    return followers

# Get the previous number of followers
def getPreviousFollowers():
    # Connect to the database
    conn = BD.connectToDatabase()
    # Create a cursor
    cursor = conn.cursor()
    # Execute the query
    cursor.execute("SELECT * FROM followers ORDER BY id DESC LIMIT 1")
    # Get the result
    result = cursor.fetchone()
    # Close the connection
    conn.close()
    # Return the result
    return result[0] 

# Get the numbers of followers and compare it with the previous number of followers  
def compareFollowers():
    # Get the number of followers
    followers = getFollowers()
    # Get the previous number of followers
    previousFollowers = getPreviousFollowers()
    # Compare the number of followers with the previous number of followers
    if followers > previousFollowers:
        # If the number of followers is greater than the previous number of followers, return true
        return True
    else:
        # If the number of followers is less than the previous number of followers, return false
        return False