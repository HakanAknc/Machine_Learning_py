import math
s = input("Ad ve Soyad giriniz: ")

s = s.replace(" ","")  # reaplece boşluk bırakmaya izin vermez

liste = []

for i in s:
    liste.append(i)

print(liste)
k = set(liste)
print(k)

d = {}  # # Boş bir sözlük oluşturulur. Bu sözlük, karakterlerin frekans oranlarını tutacaktır.

for i in k:
    adet = liste.count(i)  # # Her bir karakterin kaç kez geçtiğini sayar.
    oran = adet/len(liste)  #  # Her bir karakterin toplam karakterlere oranını hesaplar.
    d.update({i:oran})  # # Sözlüğe karakteri anahtar, oranı değer olarak ekler.

print(d)

shannon = 0

for i in d:
    v = d[i]
    shannon += v*math.log(v,2)

shannon *=-1;
print(shannon)

bs = math.ceil(shannon)  # yukarı yuvarlama yapar
print("Bit sayısı = ", bs)

dk = list(k)

b = []
for i in range(int(math.pow(2,bs))):
    a = bin(i)[2:]  # Her sayıyı ikilik (binary) sayı sistemine çevirir.
    b.append(a)

dk.sort()  # Benzersiz karakter listesini sıralar.
print(dk)
print(b)

for i in range(len(b)):
    for j in range(bs-len(b[i])):
        b[i] = "0"+b[i]

print(b)

coded = ""
for i in liste:
    coded += b[dk.index(i)]+"-"

print(coded)