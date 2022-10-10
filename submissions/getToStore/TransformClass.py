import pandas as pd

class Transform:

    @staticmethod
    def transformValues(listValue):
        for elem in listValue:
            if 'genres' in elem: 
                elem['genres'] = elem['genres'][0] if len(elem['genres']) > 0 else 'genre not specified'
            if 'external_urls' in elem:
                elem['external_urls'] = elem['external_urls']['spotify']
            if 'followers' in elem:
                elem['followers'] = elem['followers']['total']
            if 'images' in elem:
                elem['images'] = elem['images'][0]['url']

    @staticmethod
    def checkAndCleanNull(tableName: str, dataFrame: list):
        print("_________________________")
        print(f"{tableName} data frame before cleaning")
        print("_________________________")
        print(dataFrame.isnull().sum())

        dataFrame.dropna(inplace=True)

        print("_________________________")
        print(f"{tableName} data frame after cleaning")
        print("_________________________")
        print(dataFrame.isnull().sum())
    
    @staticmethod
    def getDataFrame(data: list):
        dataFrame = pd.DataFrame(data)
        return dataFrame

    @staticmethod
    def renameColumns(dataFrame, schemaColumns: dict):
        columns = Transform.getColumnNames(dataFrame)
        columnDict = {}
        for column in columns:
            if column in schemaColumns:
                columnDict[column] = schemaColumns[column]
        dataFrame.rename(columns=columnDict, inplace=True)


    @staticmethod
    def getColumnNames(dataFrame):
        columns = dataFrame.columns.values.tolist()
        return columns
    
    @staticmethod
    def dropColumns(dataFrame, schemaColumns: dict):
        columnsToDrop = []
        columns = Transform.getColumnNames(dataFrame)
        for column in columns:
            if column not in schemaColumns:
                columnsToDrop.append(column)

        dataFrame.drop(columnsToDrop, axis = 1, inplace=True)
