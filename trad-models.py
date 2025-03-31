from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

vectorizer = TfidfVectorizer(max_features=5000)
X_train = vectorizer.fit_transform(textos_treino)
clf = LinearSVC().fit(X_train, rotulos_treino)
