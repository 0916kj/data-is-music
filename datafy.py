#!/usr/bin/env python

import csv
import numpy

data = []
storedLength = 0

with open(ARGV[0]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        numericizedrow = []
        for column in row:
            try:
                numericizedrow.append(float(column))
            except:
                # ignore
        if len(numericizedrow) == 0:
            continue
        if storedLength == 0:
            storedLength = len(numericizedrow)
        if len(numericizedrow) != storedLength:
            print("Warning: skipping differently sized row")
            continue
        numericizedrow = numericizedrow[0:4]
        numericizedrow.append([0.0] * 4 - len(numericizedrow))
        data.append(numericizedrow)

npdata = numpy.array(data, dtype=numpy.single)
npmean = data.mean(axis=1)
data -= npmean
npstd = data.std(axis=1)
data /= npstd * 2
print(data)
