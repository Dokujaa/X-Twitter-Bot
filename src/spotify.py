import os
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# Setup
folder_path = 'tracks_data'
os.makedirs(folder_path, exist_ok=True)




# Get an access token from the Spotify API

def requestAPI(ids, secret):
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={'grant_type': 'client_credentials'},
        auth=(ids, secret)
    )

    response.raise_for_status()  # Raise an error for bad HTTP status codes
    access_token = response.json()['access_token']

    # Set up the headers for the HTTP GET request
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    # Send the HTTP GET request to the Spotify API for the top tracks
    response = requests.get(
        'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks?limit=50',
        headers=headers
    )

    response.raise_for_status()
    top_tracks = response.json()['items']
    return top_tracks

# Extract track data

def extract_data(top_tracks):
    track_data = []
    for i, track in enumerate(top_tracks):
        rank = str(i + 1)
        name = track['track']['name']
        artists = ', '.join([artist['name'] for artist in track['track']['artists']])
        popularity = track['track']['popularity']
        
        # Append the extracted data to the list
        track_data.append([rank, name, artists, popularity])

    # Get current date for the filename
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Save to CSV with the current date in the filename
    csv_file_path = os.path.join(folder_path, f'top_tracks_{current_date}.csv')
    df = pd.DataFrame(track_data, columns=['Rank', 'Track Name', 'Artists', 'Popularity'])
    df.to_csv(csv_file_path, index=False)

    print(f"Data saved to {csv_file_path}")





