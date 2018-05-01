import os, glob
import csv
import math



i = 0

# neg
with open("./result.txt", "r") as result_file:
    # print(result_file.read())
    array_sult = []

    # Determine si la prédiction est positive ou negative
    for f in result_file:
        if float(f) < 0.5 :
            array_sult.append(0)
        else : 
            array_sult.append(1)


index = 0
true_neg = 0
false_neg = 0
true_pos = 0
false_pos = 0

# Calcul des TP, FP, TN, FN
for x in array_sult:
    index += 1
    if index < 5000:
        if x == 0:
            true_neg += 1
        else :
            false_neg += 1
    else :
        if x == 1 :
            true_pos +=1
        else: 
            false_pos +=1

print("true_pos")
print(true_pos)

print("true_neg")
print(true_neg)

print("false_pos")
print(false_pos)

print("false_neg")
print(false_neg)

print("accuracy")
print((float(true_pos) + float(true_neg)) / (float(true_pos) + float(true_neg) + float(false_pos) + float(false_neg))) 

print("precision")
print((float(true_pos)) / (float(true_pos) + float(false_pos))) 

print("rappel")
print((float(true_pos)) / (float(true_pos) + float(false_neg))) 



