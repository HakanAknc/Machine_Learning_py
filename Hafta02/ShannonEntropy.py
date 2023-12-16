import math
s = input("Ad ve Soyadınızı giriniz:")

s = s.replace(" ","")  # Bu satır, girişteki boşlukları kaldırarak sadece karakterleri içeren bir string elde eder.

liste = []

for i in s:   # Girilen metni karakter karakter böler ve her karakteri liste adlı listeye ekler.
    liste.append(i)

print(liste)
k = set(liste)  # bir küme (set) oluşturur ve bu küme içindeki benzersiz karakterleri ekrana yazdırı
print(k)

d = {}

#Bu bölüm, her bir benzersiz karakterin girişte kaç kez geçtiğini ve bu karakterin oranını hesaplar, sonra bunları bir sözlük olan d içine ekler.
for i in k:
    adet = liste.count(i)
    oran = adet/len(liste)
    d.update({i:oran})

print(d)

shannon = 0

for i in d:
    v = d[i]
    shannon += v*math.log(v,2)

shannon *= -1

print(shannon)

bs = math.ceil(shannon)   # Shannon entropisinin üst değerini alır (yukarıya doğru yuvarlar) ve bu, bit sayısı olarak kullanılır.
print("Bit sayısı = ", bs)

dk = list(k)

b = []
for i in range(int(math.pow(2,bs))):
    a = bin(i)[2:]
    b.append(a)

dk.sort()
print(dk)
print(b)

for i in range(len(b)):
    for j in range(bs-len(b[i])):
        b[i] = "0"+b[i]

print(b)

coded = ""
for i in liste:
    coded += b[dk.index(i)]

print(coded)