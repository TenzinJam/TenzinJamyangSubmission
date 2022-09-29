Onramp Spotify/Data Engineering Project For Vanguard


This project uses Spotify data and stores that data into a persistent database. This steps are:

1) Ingestion: 
2) Tranformation:
3) Storage:
4) Visualization and Analysis: 


Technologies used:

Language: Python3
Third Party Modules: Pandas, Pprint, Spotipy
Internal Modules: Matplotlib


Project File Organization: 



<img width="331" alt="Screen Shot 2022-09-29 at 1 59 27 PM" src="https://user-images.githubusercontent.com/67336130/193118393-1da5826a-324b-40b3-afea-c2f5cfa071a5.png">


The entire project is encapsualted in the 'submissions' folder and the project is broked down into:

1) createData.py(file): this file contains all the script that takes care of 
          a) Ingenstion: 
                    - establishing the connection to Spotify API service through spotify library and its methods
                    - retrieving Spotify Data: my top 20 artists, these artists' albums, these albums' tracks and these tracks' audio features
          b) Transformation:
                    - some parts of the data transformation happens during data retrieval from Apotify as we are removing the albums that are duplicated
                    - then we are transforming some values in the original api data to conform to the schema data type
                    - then we introduce Pandas to create dataframes from the transformed data to rename columns to conform to the schema column name
                      and drop tables that are not required in the schema 


2) spotipy.db(file): this file contains 
          - 4 base tables: artist, album , track, track_feature
          - 7 view tables: refer to "viewQueries" folder to see the list of READ queries for view tables in spotify.db

3) viewQueries(folder): contains all the queries used to create the VIEW tables
          - artist_popularity: ranks the artist based on their popularity score. Ordered By Most to Least Popular
          - artists_ranked_by_albums: ranks the artists based on the number of their albums. Ordered By Most to Least number of albums
          - artists_ranked_by_tracks: ranks the artists based on the number of their tracks. Ordered By Most to Least number of tracks
          - explicit_songs_by_artists: artists with their count of explicit songs. Ordered By Least to Most number of explicit songs. 
          - nonexplicit_songs_by_artists: artists with their count of non-explicit songs. Ordered By Most to Least number of non-explicit songs. 
          - longest_songs_by_artitsts: top ten songs of each artist based on their song's duration. ORDERED first by artist, then by the song's. duration.
          - tempo_ranked_by_artists: top 10 songs of each artists based on their song's tempo. Ordered first by artist, then by the song's duration. 
          - most_followed: all 20 artists ranked by their number of followers. Ordered by most to least number of followers. 

4) visualization(folder): contains two files:
          a) visualizationQueries.py(file): list of READ queries to create the plots out of
          b) visualizationScript.py(file): running this script with run the queries in "visualizationQueries.py" and use matplotlib methods to plot visuals 
                                           for respective data from the queries. 
          c) visualization_plots.pdf(file): collection of 4 plots created using python's matplotlib module:
                    - Bar chart of "Artists Ranked by Their Music's Energy Feature"
                    - Scatter Plot showing the "Correlation Between Artists' Valence Feature and Their Popularity" 
                    - Bar Char to show "Artists' Popularity Ranking"
                    - Simple Graph Plot to show "Fluctuations in an Artist's music's Danceability Across Years/Albums". Artist = "Drake" 
                    - Scatter Plot showing "Correlation Between Artist's Valence Feature and Number of Followers" 
                    - Try creating at least one Pie Chart. 

5) .gitignore(file): some files we don't need pushed up for security reasons:
                    - .cache
                    - visualization/__pycache__




