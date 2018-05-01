import csv
import glob, os

os.chdir("./neg2")


with open("../neg.csv", 'a') as csvfile:
	for file in glob.glob("*.txt"):
		# spamwriter : objet permettant d'ecrire dans notre csv d'output
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		file = open(file, "r") 
		doc = file.read() 
		# print(doc)
		spamwriter.writerow([doc])


