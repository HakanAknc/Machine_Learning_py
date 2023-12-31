import math

# Bu kısım, örnek bir veri setini temsil eden sl (sepal length), sw (sepal width) ve tur (tür) listelerini tanımlar.
sl = [5.3, 5.1, 7.2, 5.4, 5.1, 5.4, 7.4, 6.1, 7.3, 6.0, 5.8, 6.3, 5.1, 6.3, 5.5]
sw = [3.8, 3.7, 3.0, 3.4, 3.3, 3.9, 2.8, 2.8, 2.9, 2.7, 2.8, 2.3, 2.5, 2.5, 2.4]
tur = ["Setosa","Setosa","Virginica","Setosa","Setosa","Setosa","Virginica","Verscicolor","Virginica","Verscicolor","Virginica","Verscicolor","Verscicolor","Verscicolor","Verscicolor"]

l = float(input("Lütfen sepal length değeri giriniz:"))
w = float(input("Lütfen sepal width değeri giriniz:"))
k = int(input("Lütfen K değeri giriniz:"))

# Euclidean uzaklık formülünü kullanarak verilen sepal length (l) ve sepal width (w)
# değerine göre diğer veri noktaları ile arasındaki uzaklıkları hesaplar ve bir sözlüğe (di) ekler.
di = {}
for i in range(len(sl)):
    lfark = sl[i]-l
    wfark = sw[i]-w
    u = math.sqrt(math.pow(lfark,2)+math.pow(wfark,2))
    di.update({i:u})


#Bu kısım, hesaplanan uzaklıkları ekrana yazdırır ve bu uzaklıkları küçükten büyüğe sıralar.
print(di)
dis = {k: v for k, v in sorted(di.items(), key=lambda item: item[1])}
print(dis)


# Bu satırlar, her bir veri noktasının sepal length (sl), sepal width (sw), indeks (i), tür (tur) ve hesaplanan uzaklık (dis) değerlerini ekrana yazdırır.
for i in dis:
    print(sl[i],"  ",sw[i],"  ",i,"  ",tur[i],"  ",dis[i])


# Bu kısım, sıralanmış uzaklık listesini (dis_list) oluşturur ve en yakın K veri noktasının türünü (k_list) belirler.
dis_list = list(dis)
#print(dis_list)

k_list = []
for i in range(k):
    k_list.append(tur[dis_list[i]])

print(k_list)

# Bu kısım, K en yakın komşunun türlerini sayar ve bu sayıları versicolor, setosa ve virginica değişkenlerine atar.
versicolor = setosa = virginica = 0
versicolor = k_list.count("Verscicolor")
print(versicolor)
setosa = k_list.count("Setosa")
print(setosa)
virginica = k_list.count("Virginica")
print(virginica)


# Bu kısım, K en yakın komşuların sayılarına göre en fazla olan türü belirler ve bu türü ekrana yazdırır.
if versicolor>setosa and versicolor>virginica :
    print("Sınıflandırma sonucu= Verscicolor")
elif setosa>versicolor and setosa>virginica:
    print("Sınıflandırma sonucu= Setosa")
else:
    print("Sınıflandırma sonucu= Virginica")