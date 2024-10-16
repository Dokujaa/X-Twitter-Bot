import os
from dotenv import load_dotenv, find_dotenv
from dfhandler import create_dataframe_from_csv, generate_tweet_message
from spotify import requestAPI, extract_data
from twitter import request_X_API, connect_to_oauth
from datetime import datetime

folder_path = 'tracks_data'

current_dir = os.path.dirname(os.path.abspath(__file__))


project_root = os.path.dirname(current_dir)

csv_directory = os.path.join(project_root, "tracks_data")

os.makedirs(folder_path, exist_ok=True)

load_dotenv() #Enter the path to your .env

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")



today_date = datetime.now().strftime('%Y-%m-%d')


csv_filename = f'top_tracks_{today_date}.csv'
csv_filepath = os.path.join(csv_directory, csv_filename)

if not os.path.exists(csv_filepath):
    data = requestAPI(client_id, client_secret)
    extract_data(data)
else:
    print(f"CSV file for {today_date} already exists, proceeding with existing data.")


df = create_dataframe_from_csv(csv_directory)
tweet_message = generate_tweet_message(df)

payload = {"text": tweet_message}


connect_to_oauth(consumer_key=consumer_key, consumer_secret=consumer_secret,access_token=access_token, access_token_secret=access_token_secret,payload=payload)
#request_X_API(consumer_key=consumer_key, consumer_secret=consumer_secret, payload=payload)



