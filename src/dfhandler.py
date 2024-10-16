import os
import pandas as pd
import datetime


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
    """Parses the DataFrame to generate the tweet message for the top-ranked track."""
    # Get the top-ranked track (Rank 1)
    top_track = df[df['Rank'] == 1].iloc[0]

    # Format the artist names
    artist_names = top_track['Artists'].split(", ")
    artist_names_text = " and ".join(artist_names) if len(artist_names) > 1 else artist_names[0]

    # Extract the track name and popularity
    track_name = top_track['Track Name']
    popularity = top_track['Popularity']

    # Get today's date in "Month DD, YYYY" format for the tweet
    today_date = datetime.datetime.now().strftime("%B %d, %Y")

    # Create and return the tweet message
    return f"\"{track_name}\" by {artist_names_text} is currently rank 1 on Spotify on {today_date}, with a popularity score of {popularity}! TESTSTS"
