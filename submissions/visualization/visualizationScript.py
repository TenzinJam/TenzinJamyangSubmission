import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from matplotlib import style
from pprint import pprint
from visualizationQueries import queries

conn = sqlite3.connect('spotify.db')

def dbQuery(query): 
    return pd.read_sql_query(query, con=conn)

# print(df.head(20))
# this method is to get those two arrays needed to represent the x and y values for our graph plots
def getArrays(data):
    # We are getting the column names from our data
    columns = data.columns.values.tolist()
    #  then returning the list of x values and the list of y values here. The third list is not necessary, but here to get artist_name in aggregate queries
    thirdList = data[columns[2]].to_list() if len(columns) > 2 else [0]
    return (data[columns[0]].to_list(), data[columns[1]].to_list(), thirdList[0])

# the high level method that calls all the other methods to create the visualizations
def plotVisuals(query, plotType, xlab, ylab, plotTitle, color):
    print(plotType)
    data = dbQuery(query)
    (xData, yData, optional) = getArrays(data)

    if plotType == "bar":
        plt.figure(figsize=(10,5))
        plt.bar(xData, yData, color=color)
    if plotType ==  "plot":
        plt.plot(xData, yData, color=color, label=f'Artist: {optional}')
    if plotType ==  "pie":
        plt.pie(xData, yData, color=color)
    if plotType ==  "scatter":
        plt.scatter(xData, yData, color=color)

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend()
    plt.title(plotTitle, fontsize=18)

    # this is to check if the x ticks are long strings. If it is we want to lay it out verticall, so it doesn't clutter each other and make it illegible 
    if type(xData[0]) == str:
        plt.xticks(xData, rotation='vertical')
    plt.show()

# giving users the options to pick from. Variables in call caps to show that these are constable values and created to avoid any human mistakes such as typos which the compiler
# cannot catch as an error 
BAR =  "bar"
PLOT = "plot" 
PIE = "pie" 
SCATTER = "scatter"

#  We can plot the visuals now. But before you do so, look at the method arguments and their order to understand what we need to run a plot successfully. Then you can
#  uncomment the method invocations one at a time to look at a single visualization created by matplotlib

#                       plotVisuals(data, plotType, xlabel, ylable, title, color)

# plotVisuals(queries[0], BAR, "Artists", "Popularity", "Artists Popularity Ranking", "y")
# plotVisuals(queries[1], BAR, "Artists", "Average Energy", "Artists Ranked by Their Music's Energy", "g")
# plotVisuals(queries[2], PLOT, "Album Release History", "Music's Danceability", "Fluctuation in an Artist's Music Danceability Across Albums/Years", "orange")
plotVisuals(queries[3], SCATTER, "Music's Valence", "Artist's Popularity", "Correlation Between Valence and Popularity", "b")
# plotVisuals(queries[4], SCATTER, "Music's Valence", "Artist's Popularity", "Correlation Between Valence and Popularity", "b")