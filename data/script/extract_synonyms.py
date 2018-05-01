import nltk
import re
import string
from string import punctuation
import pandas as pd
import csv
import sys
import timeit
from nltk import word_tokenize
from nltk.corpus import wordnet
from itertools import chain


input_file = "./DONE/tbfms_oa.csv"
output_file = "./DONE/s.csv"


# Analyse morpho-syntaxique du text
def syn(text):
    result = []
    for word in text:
        # print(word, " : \n")
        result.append(word)
        synonyms = wordnet.synsets(word)
        lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
        # print(lemmas)
        for l in lemmas:
            # print(l)
            result.append(l)
    return result


# Barre de chargement, initialisation du timer
animation = "|/-\\"
start = timeit.default_timer()

# Traite le premier document qui se trouve dans les header du csv input
first_doc = (' '.join(pd.read_csv(input_file, nrows=1, delimiter="\t").columns))
wordList = re.sub("[^\w]", " ",  first_doc).split()
wordList = syn(wordList)
first_doc = (' '.join(wordList))

# Ouvre le fichier d'output
with open(output_file, 'w') as csvfile:
    # spamwriter : objet permettant d'ecrire dans notre csv d'output
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([first_doc])

    # Charge le csv input dans une dataframe panda
    df = pd.read_csv(input_file, delimiter="\t")
    for i in range(9999):
        doc = (((df.iloc[i][0])))
        wordList = re.sub("[^\w]", " ",  doc).split()
        # extrait les synonymes
        wordList = syn(wordList)
        doc = (' '.join(wordList))
        spamwriter.writerow([doc])
        # Barre de chargement
        sys.stdout.write("\r" + animation[i % len(animation)] + str(i+1) + "/10 000")
        sys.stdout.flush()

# Affiche le temps d'execution
sys.stdout.write("\r" + "DONE. \n")
sys.stdout.flush()
stop = timeit.default_timer()
print(str(stop - start) , ("secondes."))
