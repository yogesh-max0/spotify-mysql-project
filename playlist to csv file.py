import mysql.connector
import pandas as pd

# MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spotify'
}

connection = mysql.connector.connect(**db_config)

# Read the table into pandas DataFrame
df = pd.read_sql("SELECT * FROM spotify_tracks", connection)

# Save as CSV
df.to_csv("spotify_playlist_data.csv", index=False)

connection.close()
print("CSV file saved in project folder!")
