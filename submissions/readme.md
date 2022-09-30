# Onramp Spotify/Data Engineering Project For Vanguard

## INTRODUCTION
This project uses Spotify data and stores that data into a persistent database after following four important steps generally practiced in data engieering. These steps are:
1. Ingestion:     
   - The stage where we establish connection to spotify api and retrieve data from Spotify's database. 
2. Tranformation:   
   - This is where we take the data return from the api calls and transform it:       
      - remove duplicate data       
      - change the data from objects or lists to primitive values such as string or integer       
      - comform the table and column names according to schema requirements      
      - drop columns we don't need to seed      
      - check for null values and drop columns with null values      
      - finally we prepare the data ready for database seeding    
3. Storage:   
   - We establish the connection with our database here   
   - create our database and insert our tables
4. Visualization and Analysis:    
   - At this stage, we have a reliable database with consistent tables and we need to:     
      - create VIEW tables to make querying quicker for future purposes     
      - create graph plots using matplotlib so that the data makes more sense to our clientele or for better internal reviews.

### Data Evolution From Ingestion To Right Before Storage: 
***The screenshots below show the story of artist table data of artist "Raveena".*** 
- After Ingestion:  
<img width="693" alt="Screen Shot 2022-09-28 at 3 28 28 PM" src="https://user-images.githubusercontent.com/67336130/193137622-381e0603-5bd2-4233-abef-c010c15d3d15.png">
- After Transformation: 
<img width="559" alt="Screen Shot 2022-09-28 at 3 28 49 PM" src="https://user-images.githubusercontent.com/67336130/193137498-7e1d70b4-7e55-44e1-820a-d95c43b7dbe9.png">
- Right Before Seeding(Storage): 
<img width="1335" alt="Screen Shot 2022-09-28 at 4 22 40 PM" src="https://user-images.githubusercontent.com/67336130/193138121-3273c37e-990c-4888-b08f-24d3c8384ae7.png">

- For in-depth description of the project, please refer to project repo's [main "readme" file](https://github.com/TenzinJam/TenzinJamyangSubmission/blob/main/README.md).


## Technologies used:
<details><summary>Click to Expand/Contract</summary>
   
- Language: Python3
- Third Party Modules: Pandas, Pprint, Spotipy
- Internal Modules: Matplotlib
- Database: sqlite3 (already installed with Python) 
   
</details>


## Project File Organization:

<details><summary> Click to Expand/Contract </summary>

<img width="331" alt="Screen Shot 2022-09-29 at 1 59 27 PM" src="https://user-images.githubusercontent.com/67336130/193118393-1da5826a-324b-40b3-afea-c2f5cfa071a5.png">
  
The entire project is encapsualted in the 'submissions' folder and the project is broked down into:
1. ***createData.py(file):***    
this file contains all the script that takes care of       
    - Ingenstion:      
      - establishing the connection to Spotify API service through spotify library and its methods     
      - retrieving Spotify Data: my top 20 artists, these artists' albums, these albums' tracks and these tracks' audio features   
  
    - Transformation:     
      - some parts of the data transformation happens during data retrieval from Apotify as we are removing the albums that are duplicated     
      - then we are transforming some values in the original api data to conform to the schema data type     
      - then we introduce Pandas to create dataframes from the transformed data to rename columns to conform to the schema column name and drop tables  that are not required in the schema    
    - Storage:      
      - By this point, we have data frames ready to be seeded into the database.      
      - We start by creating a database and then inserting the 4 tables into it.      
      - The "seed" method takes care of that. On top of seeding the database, this method also check for null values and drop them if found

2. ***spotipy.db(file):***    
   - this file contains:      
     - 4 base tables: artist, album , track, track_feature   
     - 7 view tables: refer to "viewQueries" folder to see the list of READ queries for view tables in spotify.db

3. ***viewQueries(folder):***    
   - contains all the queries used to create the VIEW tables      
     - artist_popularity: ranks the artist based on their popularity score. Ordered By Most to Least Popular.   
     - artists_ranked_by_albums: ranks the artists based on the number of their albums. Ordered By Most to Least number of albums.   
     - artists_ranked_by_tracks: ranks the artists based on the number of their tracks. Ordered By Most to Least number of tracks.   
     - explicit_songs_by_artists: artists with their count of explicit songs. Ordered By Least to Most number of explicit songs.    
     - nonexplicit_songs_by_artists: artists with their count of non-explicit songs. Ordered By Most to Least number of non-explicit songs.  
     - explicit_nonexplicit: artists with explicit and non_explicit count columns in the same table.
     - longest_songs_by_artitsts: top ten songs of each artist based on their song's duration. ORDERED first by artist, then by the song's. duration.   
     - tempo_ranked_by_artists: top 10 songs of each artists based on their song's tempo. Ordered first by artist, then by the song's duration.    
     - most_followed: all 20 artists ranked by their number of followers. Ordered by most to least number of followers. 
  
4. ***visualization(folder):***    
   - contains three files:      
     - visualizationQueries.py(file): list of READ queries to create the plots out of.   
   
   
     - visualizationScript.py(file): running this script with run the queries in "visualizationQueries.py" and use matplotlib methods to plot visuals for respective data from the queries. Please, uncomment the method invocation at the end to run the plotting.   
   
     - visualization_plots.pdf(file): 
        - collection of 4 plots created using python's matplotlib module:     
          - Bar chart of "Artists Ranked by Their Music's Energy Feature"     
          - Scatter Plot showing the "Correlation Between Artists' Valence Feature and Their Popularity"      
          - Bar Char to show "Artists' Popularity Ranking"     
          - Simple Graph Plot to show "Fluctuations in an Artist's music's Danceability Across Years/Albums". Artist = "Drake"      
          - Scatter Plot showing "Correlation Between Artist's Valence Feature and Number of Followers" 
  
5. ***.gitignore(file):*** 
   - some files we don't need pushed up for security reasons:   
      - .cache   
      - visualization/__pycache__
</details>


## Entity Relationship Diagram and Data Types Legend:
<details><summary> Click to Expand/Contract </summary>

![DatabaseSchema](https://user-images.githubusercontent.com/67336130/193127507-d0ae6450-5081-4208-97bc-0014492f7b7d.jpg)
  
   - This figure shows the tables in our spotify database and also specifies the datatypes of each columns. Please, note the relationship between the tables because these are what allows to combine different tables and produce new permanent and virtual tables for our easy use. 
   - Next to is the legend that lists the data types in SQLite and how they correspond to other data types prevalent in other RDBMs (Relational Database Management Systems). The data type on this schema will not match the ones in our "spotify.db" and thus this legend helps in translating that.       </details>

## Resources and Informative Articles Pertinent to Project
<details><summary> Click to Expand/Contract </summary>   
   
   
   [📺 Python, pandas, sqlite3 tutorial](https://www.youtube.com/watch?v=YyUknBHcZB8)
   
   [📺 Relevant Pandas methods](https://www.youtube.com/watch?v=tRKeLrwfUgU)
   
   [📜 Spotipy official documentation](https://spotipy.readthedocs.io/en/master/#spotipy.client.Spotify.search)
   
   [📺 Spotify credentials setup video](https://www.youtube.com/watch?v=3RGm4jALukM)
   
   [📜 Medium article on pprint](https://python.plainenglish.io/using-pprint-in-python-to-write-less-code-and-save-time-3c7329c98a7c)
   
   [📜 Why there are dublicate albums on Spotify](https://community.spotify.com/t5/iOS-iPhone-iPad/Duplicates-of-the-same-albums/td-p/4542505#:~:text=It%20looks%20like%20the%20duplicate%20albums%20are%20appearing,some%20cases%20this%20is%20duplicating%20the%20album%20instead.)
   
   [📜 Getting the correct "Scope" for Spotify API calls](https://developer.spotify.com/documentation/general/guides/authorization/scopes/#user-library-read)
   
   [📜 What are Views and the Advantages Over Base Tables](https://en.wikipedia.org/wiki/View_(SQL))
   
   [📜 Getting the correct "Scope" for Spotify API calls](https://developer.spotify.com/documentation/general/guides/authorization/scopes/#user-library-read)
   
   [📜 Matplotlib Official Documentation](https://matplotlib.org/stable/tutorials/index)
   
   
</details>

