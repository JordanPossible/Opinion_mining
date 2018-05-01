import os, glob
import csv

all_neg_path = "./ready/neg"
all_pos_path = "/ready/pos"


os.chdir("./ready/neg")
i = 12500

# Extrait les documents negatifs
with open("../../test.tsv", "w") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    # pour chaque fichier negatif, ecrit une ligne dans le tsv
    for file in glob.glob("*.txt"):
        if(i < 25000):
            f = open(file, "r") 
            content = (f.read())

            writer.writerow([str(i), str(content)])

        i = i+1
        print(i)

os.chdir("../pos")
i = 12500

# Extrait les documents positifs
with open("../../test.tsv", "a") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    # pour chaque fichier positif, ecrit une ligne dans le tsv
    for file in glob.glob("*.txt"):
        if(i < 25000):
            f = open(file, "r") 
            content = (f.read())

            writer.writerow([str(i), str(content)])
        i = i+1
        print(i)



