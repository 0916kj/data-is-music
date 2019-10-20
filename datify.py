#!/usr/local/bin/python3

import csv
import numpy
import sys
import math
import serial

data = []
storedLength = 0

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        numericizedrow = []
        for column in row:
            try:
                numericizedrow.append(float(column))
            except:
                continue
                # ignore
        if len(numericizedrow) == 0:
            continue
        if storedLength == 0:
            storedLength = len(numericizedrow)
        if len(numericizedrow) != storedLength:
            print("Warning: skipping differently sized row")
            continue
        numericizedrow = numericizedrow[0:4]
        numericizedrow.extend([0.0] * (4 - len(numericizedrow)))
        data.append(numericizedrow)

# transform into z-score, modified by standard deviation of the -1 1 uniform
# distribution
npdata = numpy.array(data, dtype=numpy.single)
npmean = numpy.median(npdata, axis=0)
npstd = numpy.std(npdata, axis = 0)
for i in range(4):
    npdata[0:,i] -= npmean[i]
    npdata[0:,i] /= max(npstd[i], numpy.finfo(numpy.single).tiny) / (2/math.sqrt(12))

# now scale -1 1 to 0, 255
npdata += 1
npdata /= 2
npdata *= 255

# round and clamp
npdata = numpy.round(npdata)
npdata = numpy.clip(npdata, 0, 255)

# cast float to integer
npdata = npdata.astype(numpy.intc)

# set up serial connection
s = serial.Serial(port='/dev/tty.usbmodemfa141', baudrate=9600)

# loop until quit
i = 0
while True:
    packet = bytearray()
    packet.append(npdata[i][0])
    packet.append(npdata[i][1])
    packet.append(npdata[i][2])
    packet.append(npdata[i][3])
    s.write(packet)
    i += 1
    if i >= len(npdata):
        i = 0
