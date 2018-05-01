import pandas as pd
import csv
import sys
import re
import string
from string import punctuation
import timeit

input_file = "./DONE/s2.csv"
output_file = "./DONE/s3.csv"

def clean_text(text):
    # transforme les mots en miniscules
    text = text.lower().split()
    text = " ".join(text)
    # nettoyage grace aux regex
    text = re.sub(r"<br />", " ", text)
    text = re.sub(r"[^a-z]", " ", text)
    text = re.sub(r"   ", " ", text) 
    text = re.sub(r"  ", " ", text)
    # on retire la ponctuation
    text = ''.join([c for c in text if c not in punctuation])
    return(text)


# Barre de chargement, initialisation du timer
animation = "|/-\\"
start = timeit.default_timer()

# Traite le premier document qui se trouve dans le header du csv
first_doc = clean_text(' '.join(pd.read_csv(input_file, nrows=1, delimiter="\t").columns))

# Ouvre le fichier d'output
with open(output_file, 'w') as csvfile:
    # spamwriter : objet permettant d'ecrire dans notre csv d'output
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([first_doc])

    # Charge le csv input dans une dataframe panda
    df = pd.read_csv(input_file, delimiter="\t")
    for i in range(9999):
        row = clean_text(df.iloc[i][0])
        spamwriter.writerow([row])
        # Barre de chargement
        sys.stdout.write("\r" + animation[i % len(animation)] + str(i+1) + "/10 000")
        sys.stdout.flush()

# Affiche le temps d'execution
sys.stdout.write("\r" + "DONE. \n")
sys.stdout.flush()
stop = timeit.default_timer()
print(str(stop - start) , ("secondes."))
