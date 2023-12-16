str1 = open("s1.txt", "r").read()
str2 = open("s2.txt", "r").read()
str3 = open("s3.txt", "r").read()

durma = [".",",","'","?","!","ve", "veya", "ile", "çünkü", "birkaç", "böyle", "falan", "herkes", "hiçbiri",
         "gibi", "hangi", "kim", "şu", "şey", "yada", "zira", "zaten", "yine", "neyse",
         "ama", "ancak", "asla", "az", "bazı", "bazısı", "belki", "birçok", "çok", "çoğu",
         "daha", "değil", "diğer", "elbette", "hiç", "ise", "kendi", "kime", "niye", "önce",
         "ötürü", "rağmen", "şunu", "şunlar", "tümü", "veya", "yoksa", "zaten", "zira"]

for i in durma:
    str1 = str1.replace(i, "")
    str2 = str2.replace(i, "")

l1 = list(str1.split(" "))
print(l1)
print(len(l1))

# Durma sözcükleri çıkarıldıktan sonra toplam kelime sayısı
l2 = list(str2.split(" "))
print(l2)
print(len(l2))

l3 = list(str3.split(" "))
print(l3)
print(len(l3))

# m1 ile m2' yi küme haline getirdim
s1 = set(l1)
print(s1)
print(len(s1))

# m1 ile m2' yi küme haline getirdim
s2 = set(l2)
print(s2)
print(len(s2))

s3 = set(l3)
print(s3)
print(len(s3))

# s1 ile s2' yi birleştiriyoruz
st = set.union(s1, s2, s3)
print(st)
print(len(st))

ts = len(s1) + len(s2) + len(s3)
print("İki metin için tekil sözcük sayısı = ", ts)
tss = len(st)
print("Birleşim sonrası tekil sözcük sayısı = ", tss)
fark = ts - tss
print("Fark = ", fark)
benzeme = (fark * 100) / tss
print("Benzeme oranı = %", benzeme)