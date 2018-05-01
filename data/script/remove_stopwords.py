import pandas as pd
import csv
import sys
import re
import timeit
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


input_file = "./DONE/tbn.csv"
output_file = "./DONE/tbnssw.csv"

# Genere la liste de stop-words customis et ajoute la liste de stop words generique
custom_stop_words = ['movie', 'film', 'story', 'people', 'movies', 'seen', 'watch', 'acting', 'films', 'characters', 
'show', 'character', 'man', 'scene', 'watching', 'scenes', 'actors', 'director', 'saw', 'series']
custom_stop_words = custom_stop_words + stopwords.words("english")
print(custom_stop_words)

# Variable globale, donne le nombre de stopwords supprimé à la fin du traitement
deleted_words = 0

# Retourne la liste des mots sans stop-words
def remove_stopwords(word_list):
        processed_word_list = []
        for word in word_list:
            if word not in custom_stop_words:
                processed_word_list.append(word)
            else:
                # print(word)
                global deleted_words
                deleted_words = deleted_words+1
        return processed_word_list

# Barre de chargement, initialisation du timer
animation = "|/-\\"
start = timeit.default_timer()

# Traite le premier document qui se trouve dans les header du csv
first_doc = (' '.join(pd.read_csv(input_file, nrows=1, delimiter="\t").columns))
# split la string en list
wordList = re.sub("[^\w]", " ",  first_doc).split()
wordList = remove_stopwords(wordList)
# remet la liste en string
first_doc = (' '.join(wordList))
# fichier d'output
with open(output_file, 'w') as csvfile:
    # spamwriter : objet permettant d'ecrire dans notre csv d'output
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([first_doc])

    # Charge le csv input dans une dataframe panda
    df = pd.read_csv(input_file, delimiter="\t")
    for i in range(9999):
        doc = df.iloc[i][0]
        # print(doc)
        # split la string en list
        wordList = re.sub("[^\w]", " ",  doc).split()
        wordList = remove_stopwords(wordList)
        # # remet la liste en string
        entry = (' '.join(wordList))
        spamwriter.writerow([entry])
        # Barre de chargement
        sys.stdout.write("\r" + animation[i % len(animation)] + str(i+1) + "/10 000")
        sys.stdout.flush()

# Affiche le temps d'execution et le nombre de mots retiré
sys.stdout.write("\r" + "DONE. \n")
sys.stdout.flush()
stop = timeit.default_timer()
print(str(deleted_words) , (" stopwords has been removed"))
print(str(stop - start) , ("secondes."))
