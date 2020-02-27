#!/usr/bin/env python3
import pandas
import os
import math


def main():
    yearlyHoursList = getYearlyHoursList()
    printDetails(yearlyHoursList)

def printDetails(hourList):
    for hours in hourList:
        print("Yearly Hours: ", hours)
    print("Overall Hours:", sum(hourList))

def getYearlyHoursList():
    csvDataFramesList = getCsvDataFramesList()
    yearlyHoursList = []
    for dataFrame in csvDataFramesList:
        hours = getHours(dataFrame)
        yearlyHoursList.append(hours)

    return yearlyHoursList

def getCsvDataFramesList():
    csvPaths = getCsvPaths()
    dataFramesList = []
    for path in csvPaths:
        dataFramesList.append(pandas.read_csv(path))

    return dataFramesList

def getCsvPaths():
    csvFolder = "csvs"
    csvNames = os.listdir(csvFolder)
    csvPaths = []
    for name in csvNames:
        path = os.path.join(csvFolder, name)
        csvPaths.append(path)
    
    return csvPaths

def getHours(dataFrame):
    dataFrame = setDurationAsHoursFloat(dataFrame)

    return dataFrame["Duration"].sum()

def setDurationAsHoursFloat(dataFrame):
    totalRows = dataFrame.shape[0]
    for i in range(totalRows):
        durationString = dataFrame.loc[i, "Duration"]
        hoursFloat = getHoursFloat(durationString)
        dataFrame.loc[i, "Duration"] = hoursFloat

    return dataFrame

def getHoursFloat(string):
    # string format: "<hr>:<min>:<sec>"
    partsAsFloats = [float(part) for part in string.split(":")]
    return \
            partsAsFloats[0] \
            + partsAsFloats[1] / 60 \
            + partsAsFloats[2] / (60*60)

if __name__ == "__main__":
    main()
