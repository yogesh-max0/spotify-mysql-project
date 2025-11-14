# spotify-mysql-project
 
This project extracts playlist data from the Spotify Web API, processes it using Python, and stores the results into a MySQL database.
It also exports the playlist tracks into a CSV file for analysis.

📌 mysql_connection.py           → Inserts playlist data into MySQL  
📌 spotify.api.py                → Collects playlist data using Spotify API  
📌 playlist to csv file.py       → Saves playlist data into a CSV file  
📌 spotify_playlist_data.csv     → Output CSV file  
📌 README.md                     → Project documentation  


🚀 Features
✔ Fetch playlist details from Spotify API
✔ Extract track name, artist, album, popularity, duration
✔ Save cleaned data to CSV file
✔ Insert playlist data into MySQL database
✔ Easy-to-understand Python scripts for beginners

🛠 Technologies Used
.Python
.Spotify Web API (Spotipy)
.MySQL
.Pandas
.Matplotlib (optional)
.MySQL Connector


⚙️ How to Run the Project
1️⃣ Install required Python libraries
pip install spotipy pandas mysql-connector-python matplotlib

2️⃣ Run the Spotify API script
This script collects playlist data:

python spotify.api.py
3️⃣ Export playlist data to CSV
python "playlist to csv file.py"

This creates:
spotify_playlist_data.csv

4️⃣ Insert data into MySQL
Make sure your MySQL database and table are created.
Then run:
python mysql_connection.py



🧩 MySQL Table Structure (Required)


CREATE DATABASE spotify;

USE spotify;

CREATE TABLE spotify_tracks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    playlist_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);



📦 Output
.A structured CSV file
.Spotify playlist records inserted into your MySQL database
.Clean and modular Python scripts for each task

👤 Author
Yogeshwaran
GitHub: https://github.com/yogesh-max0
LinkedIn: https://linkedin.com/in/yogesh-waran-496a88321
