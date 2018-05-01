from xgboost import XGBClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
import timeit

# Demarre le timer
start = timeit.default_timer()

# On utilise la methode load_files pour charger le data_set dans la variable dataset
movie_reviews_data_folder = "./txt/tbfms_oa"
dataset = load_files(movie_reviews_data_folder, shuffle=False)
print("n_samples: %d" % len(dataset.data))

# split le dataset en deux : entrainement (70) et test (30)
docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.30, random_state=None)

# Crée count_vect : l'objet avec lequel on vectorise les documents    
# count_vec = TfidfVectorizer(analyzer="word", max_features=10000, ngram_range=(1,2), sublinear_tf=True)
count_vec = TfidfVectorizer(ngram_range=(1,2))

# Vectorise le jeu d'entrainement et de test
train_vec = count_vec.fit_transform(docs_train)
test_vec = count_vec.transform(docs_test)

# Entraine GB avec les vecteurs d'entrainements
gbm = XGBClassifier(max_depth=5, n_estimators=500, learning_rate=0.05).fit(train_vec, y_train)
# y_predicted contient les labels prédit sur le jeu de test
y_predicted = gbm.predict(test_vec)

# Print les resultats de la classification
print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))

# Puis la matrice de confusion
cm = metrics.confusion_matrix(y_test, y_predicted)
print(cm)

# Stop le timer et print le temps d'execution
stop = timeit.default_timer()
print ("temps d'execution : ") + str(stop - start) + (" secondes.")
    
    
    
