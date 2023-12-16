# numpy kütüphanesini 'np' takma adıyla içe aktarın
import numpy as np

# sklearn.naive_bayes modülünden GaussianNB sınıfını içe aktarın
from sklearn.naive_bayes import GaussianNB

# Eğitim verisi 'X' ve etiketler 'Y' olarak tanımlanmıştır.
X = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 2, 1, 0],
    [2, 2, 1, 1],
    [1, 2, 1, 1],
    [0, 1, 0, 0],
    [0, 2, 1, 0],
    [2, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [2, 1, 0, 1]
])

# Eğitim verisi etiketleri
Y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

# GaussianNB sınıfından bir model oluşturun
model = GaussianNB()

# Modeli eğitim verisi üzerinde eğitin
model.fit(X, Y)

# Modeli eğittikten sonra, yeni bir örneği kullanarak tahmin yapın
# Örnek olarak [0, 0, 0, 0] kullanılmıştır
print(model.predict([[0, 0, 0, 0]]))
