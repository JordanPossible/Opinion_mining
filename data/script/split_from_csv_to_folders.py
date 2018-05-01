import re
import os, errno
import sys
import csv
import random
import string
import time
import pandas as pd
import timeit


# input_file = "./csv/s.csv"
# output_file = "./txt/s/"
# csv_list = ['tb', 'tbfms_large', 'tbfms_oa', 'tbfms_small', 'tbl', 'tbn', 'tbnssw', 'tbnsswl', 'tbogt', 's' ]
# csv_list = ['s']


# Barre de chargement, initialisation du timer, filepath du working_set
animation = "|/-\\"
start = timeit.default_timer()



input_file = "./neg.csv"
output_folder = "./ready/neg/"

# Charge le csv dans une dataFrame
df = pd.read_csv(input_file, sep='\n')
# Met le premier document sous forme de texte et l'ecrit dans le fichier de sortie(il est dans le header du csv)
outfile = output_folder + "o" + ".txt"
file=open(outfile, "w+")
file.write(''.join(df.head(0)))
file.close()

	# Chaque ligne du csv engendre un fichier texte
i = 0
while(i<29999):
	outfile = output_folder + str(i) + ".txt"
	file=open(outfile, "w+")
	file.write(''.join(df.iloc[i][0]))
	file.close()
	sys.stdout.write("\r" + animation[i % len(animation)] + str(i) + "/30 000")
	sys.stdout.flush()
	i = i+1

print(csv, " is DONE.")



		# sys.stdout.write("\r" + "DONE. \n")
		# sys.stdout.flush()

# Affiche le temps d'execution
stop = timeit.default_timer()
timeExec = str(stop - start)
print ("temps d'execution : ", timeExec, "secondes.")
print(stop - start)