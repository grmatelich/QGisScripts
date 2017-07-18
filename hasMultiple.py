#!/usr/local/bin/python

import re
import os
import sys

fileList = [] 

for filename in os.listdir(os.getcwd()):
    #print(filename)
    fileList.append(filename)

#print(fileList)

pattern = re.compile(".*geojson")

bad = []

for geo in fileList:
    if pattern.match(geo):
        #print(geo)
        temp = open(geo, "r")
        words = temp.read()
        temp.close()
        match = re.findall('"centroid_x":([^,]+)', words)
    
        if len(match) > 1:
            bad.append(geo)
            #print('YES')
            #print(len(match))

print(bad)



        
