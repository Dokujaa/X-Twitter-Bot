import datetime
import os
import pandas as pd
import random

def create_dataframe_from_csv(csv_directory):
    today_date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

    matching_files = [f for f in csv_files if today_date_str in f]

    # Check if there are matching files
    if not matching_files:
        raise FileNotFoundError(f"No CSV file found for today's date: {today_date_str}")

    # Use the first matching file
    csv_file_path = os.path.join(csv_directory, matching_files[0])

    return pd.read_csv(csv_file_path)

def generate_tweet_message(df):
    """Parses the DataFrame to generate a random tweet message with specific rank for a track."""
    # Randomly select a row from the DataFrame
    random_track = df.sample(n=1).iloc[0]

    # Get the specific rank
    rank = random_track['Rank']

    # Format the artist names
    artist_names = random_track['Artists'].split(", ")
    artist_names_text = " and ".join(artist_names) if len(artist_names) > 1 else artist_names[0]

    # Extract the track name and popularity
    track_name = random_track['Track Name']
    popularity = random_track['Popularity']

    # Get today's date in "Month DD, YYYY" format for the tweet
    today_date = datetime.datetime.now().strftime("%B %d, %Y")

    # Create and return the tweet message
    return f"\"{track_name}\" by {artist_names_text} is currently ranked #{rank} on Spotify on {today_date}, with a popularity score of {popularity}!"


