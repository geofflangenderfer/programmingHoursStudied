#!/usr/bin/env python3
from hoursStudied import *

def testGetYearlyHoursList():
    assert abs(
            sum(getYearlyHoursList()) 
            - 1851.729444444444
           ) < .0001

if __name__ == "__main__":
    testGetYearlyHoursList()
