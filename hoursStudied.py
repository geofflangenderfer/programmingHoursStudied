#!/usr/bin/env python3
import pandas
import os

def main():
    totalHours = getTotalHours()
    print("Overall:", totalHours)

def getTotalHours():
    csvDataFramesList = getCsvDataFramesList()
    total = 0
    for dataFrame in csvDataFramesList:
        hours = getHours(dataFrame)
        print("Yearly Hours:", hours, "\n")
        total += hours

    return total

def getCsvDataFramesList():
    csvPaths = getCsvPaths()
    dataFramesList = []
    for path in csvPaths:
        dataFramesList.append(pandas.read_csv(path))

    return dataFramesList

def getCsvPaths():
    allPaths = os.listdir(".")
    csvPaths = []
    for path in allPaths:
        if isCsv(path):
            csvPaths.append(path)
    
    return csvPaths

def isCsv(path):
    return path.split(".")[-1] == "csv"

def getHours(dataFrame):
    dataFrame = setDurationAsHoursFloat(dataFrame)

    return dataFrame["Duration"].sum()

def setDurationAsHoursFloat(dataFrame):
    totalRows = dataFrame.shape[0]
    for i in range(totalRows):
        duration = dataFrame.loc[i, "Duration"]
        hoursFloat = getHoursFloat(duration)

        dataFrame.loc[i, "Duration"] = hoursFloat

    return dataFrame





def getHoursFloat(string):
    # string format: hr:min:s
    partsAsFloats = [float(part) for part in string.split(":")]
    return \
            partsAsFloats[0] \
            + partsAsFloats[1] / 60 \
            + partsAsFloats[2] / (60*60)

if __name__ == "__main__":
    main()

