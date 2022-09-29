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

The entire project is encapsualted in the 'submissions' folder and the project is broked down into:

1) createData.py file: this file contains all the script that takes care of 
          - establishing the connection to Spotify API service through spotify library and its methods
          - retrieving Spotify Data: my top 20 artists, these artists' albums, these albums' tracks and these tracks' audio features
          - some parts of the data transformation happens at this stage as we are removing the albums that are duplicated 


2) spotipy.db: this file contains 
          - 4 base tables: artist, album , track, track_feature
          - 7 view tables: 
