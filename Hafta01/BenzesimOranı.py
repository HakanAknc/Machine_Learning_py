# m1.txt ve m2.txt adlı iki metin dosyasını okuma modunda açıp, içeriklerini sırasıyla str1 ve str2 adlı stringlere okuyor.
str1 = open('m1.txt', 'r').read()   #.read(): Dosyanın içeriğini okur ve bir dize olarak str1 değişkenine atar.
str2 = open('m2.txt', 'r').read()

durma = [".",",","'","?","!","ve", "veya", "ile", "çünkü", "birkaç", "böyle", "falan", "herkes", "hiçbiri",
         "gibi", "hangi", "kim", "şu", "şey", "yada", "zira", "zaten", "yine", "neyse",
         "ama", "ancak", "asla", "az", "bazı", "bazısı", "belki", "birçok", "çok", "çoğu",
         "daha", "değil", "diğer", "elbette", "hiç", "ise", "kendi", "kime", "niye", "önce",
         "ötürü", "rağmen", "şunu", "şunlar", "tümü", "veya", "yoksa", "zaten", "zira"]

#durma listesindeki her bir kelime veya karakteri str1 ve str2 içinde bulunan metinlerden çıkarır.
for i in durma:
    str1 = str1.replace(i, "")
    str2 = str2.replace(i, "")

# Bu kısım, str1 ve str2 içindeki metinleri boşluklara göre ayırarak, her bir kelimeyi içeren listeleri oluşturur ve bu listeleri ekrana yazdırır.
l1 = list(str1.split(" "))
print(l1)
print(len(l1))

# Durma sözcükleri çıkarıldıktan sonra toplam kelime sayısı
l2 = list(str2.split(" "))
print(l2)
print(len(l2))

# m1 ile m2' yi küme haline getirdim
s1 = set(l1)
print(s1)
print(len(s1))

# m1 ile m2' yi küme haline getirdim
s2 = set(l2)
print(s2)
print(len(s2))

# s1 ile s2' yi birleştiriyoruz
st = set.union(s1, s2)
print(st)
print(len(st))

ts = len(s1) + len(s2)
print("İki metin için tekil sözcük sayısı = ", ts)
tss = len(st)
print("Birleşim sonrası tekil sözcük sayısı = ", tss)
fark = ts - tss
print("Fark = ", fark)
benzeme = (fark * 100) / tss
print("Benzeme oranı = %", benzeme)
