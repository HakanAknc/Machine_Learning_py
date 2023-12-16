import numpy as np    # Bu satır, numpy kütüphanesini içe aktarır.
from sklearn.naive_bayes import GaussianNB
# Bu satır, sklearn kütüphanesinin GaussianNB sınıfını içe aktarır.

A = np.array([
              [0, 0, 0, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0],
              [2, 1, 0, 0],
              [2, 2, 1, 0],
              [2, 2, 1, 1],
              [1, 2, 1, 1],])

B = np.array([0, 0, 1, 1, 1, 0, 1])
"""
A ve B dizileri, eğitim verilerini ve etiketlerini temsil eder. 
A dizisi, özellikleri içerir ve her satır bir veri noktasını temsil eder. 
B dizisi, bu veri noktalarının sınıf etiketlerini içerir.
"""

model = GaussianNB()   # Bu satır, Gaussian Naive Bayes modelini oluşturur.
model.fit(A, B)

print(model.predict([[0, 0, 1, 1]]))
#  Bu satır, eğitilen modeli kullanarak veri noktasının sınıfını tahmin eder.

