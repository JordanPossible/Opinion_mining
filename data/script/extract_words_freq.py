from nltk import FreqDist
import pandas as pd
import csv
import sys
import re
import timeit
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


input_file = "./tb.csv"
output_file = "./corpus_stats.csv"


# Barre de chargement, initialisation du timer
animation = "|/-\\"
start = timeit.default_timer()

all_words_in_corpus_list = []

 # extrait le premier doc
first_doc = (' '.join(pd.read_csv(input_file, nrows=1, delimiter="\t").columns))
# split le doc
wordList = re.sub("[^\w]", " ",  first_doc).split()
for word in wordList:
	all_words_in_corpus_list.append(word)

# Charge le csv input dans une dataframe panda
df = pd.read_csv(input_file, delimiter="\t")
for i in range(9999):
	doc = (((df.iloc[i][0])))
	wordList = re.sub("[^\w]", " ",  doc).split()
	for word in wordList:
		all_words_in_corpus_list.append(word)
	sys.stdout.write("\r" + animation[i % len(animation)] + str(i+1) + "/10 000")
	sys.stdout.flush()

# On met en minuscule pour eviter de compter 'The' et 'the' comme deux mots differents
# Et on supprimer les stop-words
lowered_without_sw = []

print("Start filtering stop-words ...")
for word in all_words_in_corpus_list:
	word = word.lower()
	if word not in stopwords.words("english"):
		lowered_without_sw.append(word)
		# print(word)

# Extrait le ranking de la liste de tous les mots 
print("Start ranking words ...")
wordRanking = (Counter(lowered).most_common())
print("Ranking is DONE.")

# Ecrit le resultat dans output_file
with open(output_file, 'w') as csvfile:
    # spamwriter : objet permettant d'ecrire dans notre csv d'output
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for words in wordRanking:
    	# print(words)
    	spamwriter.writerow([words])

