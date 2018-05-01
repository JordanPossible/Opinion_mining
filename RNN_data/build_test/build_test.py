import os, glob
import csv



i = 0
os.chdir("./neg")

# extrait les documents negatifs
with open("../test.tsv", "w") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    # pour chaque fichier negatif, ecrit une ligne dans le tsv
    for file in glob.glob("*.txt"):
        f = open(file, "r") 
        content = (f.read())

        writer.writerow([str(i), str(content)])
        i = i + 1
        print(i)


os.chdir("../pos")

# extrait les documents positifs
with open("../test.tsv", "a") as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')

    # pour chaque fichier positif, ecrit une ligne dans le tsv
    for file in glob.glob("*.txt"):
        f = open(file, "r") 
        content = (f.read())

        writer.writerow([str(i), str(content)])
        i = i + 1
        print(i)



