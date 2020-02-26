#!/usr/bin/env python3
import pandas
import os
from datetime import datetime

def main():
    totalHours = getTotalHours()
    print("Overall:", totalHours)

def getTotalHours():
    csvDataFramesList = getCsvDataFramesList()
    total = 0
    for dataFrame in csvDataFramesList:
        hours = getHours(dataFrame)
        printDetails(dataFrame, hours)
        total += hours

    return total

def printDetails(dataFrame, hours):
    #print("Snapshot:\n", dataFrame.head(), "\n")
    print("Yearly Hours:", hours, "\n")

def getCsvDataFramesList():
    csvPaths = getCsvPaths()
    dataFrames = []
    for path in csvPaths:
        dataFrames.append(pandas.read_csv(path))

    return dataFrames

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
            + partsAsFloats[0] / 60 \
            + partsAsFloats[0] / (60*60)

if __name__ == "__main__":
    main()

