import os, glob
import csv
import math



i = 0

# neg
with open("./result.txt", "r") as result_file:
    # print(result_file.read())
    array_sult = []

    for f in result_file:
        if float(f) > 0.8 :
            array_sult.append(1)
        else : 
            array_sult.append(0)




index = 0
good = 0
bad = 0


for x in array_sult:
    index += 1
    if x == 1:
        good += 1
    else :
        bad += 1
        

print(" > 0.8")
print(good)

print("< 0.8")
print(bad)

print("accuracy")
print((float(good)) / (float(bad) + float(good))) 
