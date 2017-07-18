#!/usr/local/bin/python

import re
import os
import sys

fileList = [] 

#for each file in CWD
for filename in os.listdir(os.getcwd()):
    #print(filename)
    fileList.append(filename)

#print(fileList)

#check for all of the geojson files with a regex
pattern = re.compile(".*geojson")

bad = []

#for each file
for geo in fileList:
    #if geojson
    if pattern.match(geo):
        #print(geo)
        #read the file
        temp = open(geo, "r")
        words = temp.read()
        temp.close()
        
        #file all instances of centroid_x in this case
        match = re.findall('"centroid_x":([^,]+)', words)
    
        #if occurs multiple times, then add this to the list of corrupted files
        if len(match) > 1:
            bad.append(geo)
            #print('YES')
            #print(len(match))

#print such corrupted files
print(bad)



        
