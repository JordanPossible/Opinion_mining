import os, glob
import csv

all_neg_path = "./ready/neg"
all_pos_path = "/ready/pos"


os.chdir("./ready/neg")
i = 0

# Extrait les documents negatifs
with open("../../train.tsv", "w") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    # pour chaque fichier negatif, ecrit une ligne dans le tsv
    for file in glob.glob("*.txt"):
        if(i < 12500):
            f = open(file, "r") 
            content = (f.read())

            writer.writerow([str(i), str(0), str(content)])

        i = i+1
        print(i)

os.chdir("../pos")
i = 0

# Extrait les documents positifs
with open("../../train.tsv", "a") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    # pour chaque fichier positif, ecrit une ligne dans le tsv
    for file in glob.glob("*.txt"):
        if(i < 12500):
            f = open(file, "r") 
            content = (f.read())

            writer.writerow([str(i), str(1), str(content)])
            
        i = i+1
        print(i)

