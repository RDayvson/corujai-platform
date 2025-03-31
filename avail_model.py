from sklearn.metrics import classification_report

predicoes = model.predict(X_test)
print(classification_report(y_test, predicoes))
