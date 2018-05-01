from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import csv
import sys
import timeit
import re

nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()


input_file = "./DONE/tbnssw.csv"
output_file = "./DONE/tbnsswl.csv"

# Barre de chargement, initialisation du timer
animation = "|/-\\"
start = timeit.default_timer()
lemmatized_words = 0

# lematize la liste de mots
def lematize(word_list):
    processed_word_list = []
    for word in word_list:
        canonical_shape = wordnet_lemmatizer.lemmatize(word, pos='v')
        # print("word ", word, " : ", canonical_shape)
        if(canonical_shape != word):
            # incremente le compteur
            global lemmatized_words
            lemmatized_words = lemmatized_words+1
        processed_word_list.append(canonical_shape)
    return processed_word_list

# Traite le premier document qui se trouve dans les header du csv
first_doc = (' '.join(pd.read_csv(input_file, nrows=1, delimiter="\t").columns))
# split la string en list
wordList = re.sub("[^\w]", " ",  first_doc).split()
# remet la liste en string
wordList = lematize(wordList)
first_doc = (' '.join(wordList))
# fichier d'output
with open(output_file, 'w') as csvfile:
    # spamwriter : objet permettant d'ecrire dans notre csv d'output
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([first_doc])

    # Charge le csv input dans une dataframe panda
    df = pd.read_csv(input_file, delimiter="\t")
    for i in range(9999):
        doc = (((df.iloc[i][0])))
        # split la string en list
        wordList = re.sub("[^\w]", " ",  doc).split()
        wordList = lematize(wordList)
        # remet la liste en string
        doc = (' '.join(wordList))
        spamwriter.writerow([doc])
        # Barre de chargement
        sys.stdout.write("\r" + animation[i % len(animation)] + str(i+1) + "/10 000")
        sys.stdout.flush()

# Affiche le temps d'execution et le nombre de mots lematized
sys.stdout.write("\r" + "DONE. \n")
sys.stdout.flush()
stop = timeit.default_timer()
print(str(lemmatized_words) , (" words has been lemmatized"))
print(str(stop - start) , ("secondes."))
