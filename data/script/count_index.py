import pandas as pd
import numpy as np
import nltk, re, time
from nltk.corpus import stopwords
from string import punctuation
from collections import namedtuple
from sklearn.datasets import load_files
from keras.preprocessing.text import Tokenizer

input_file = "./DONE/s.csv"

# Charge le csv dans une dataframe
dataset = pd.read_csv(input_file, delimiter="\t")
print(dataset.shape)

# Tokenize le corpus et print la longueur de l'index
tokenizer = Tokenizer()
tokenizer.fit_on_texts(dataset)
word_index = tokenizer.word_index
print("Words in index: %d" % len(word_index))



