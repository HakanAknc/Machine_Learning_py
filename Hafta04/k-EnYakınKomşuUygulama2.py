import math

sl = [5.3, 5.1, 7.2, 5.4, 5.1, 5.4, 7.4, 6.1, 7.3, 6.0,]
sw = [3.8, 3.7, 3.0, 3.4, 3.3, 3.9, 2.8, 2.8, 2.9, 2.7,]
tur = ["Hakan","Hakan","Evren","Hakan","Hakan","Eyüp","Evren","Eyüp","Evren","Hakan"]

l = float(input("Lütfen sepal length değeri giriniz: "))
w = float(input("Lütfen width length değeri giriniz: "))
k = int(input("Lütfen K değeri giriniz: "))  # K değeri en yakın kaç komşuya bakacağımızı göterir.

di = {}
for i in range(len(sl)):
    lfark = sl[i]-l
    wfark = sw[i]-w
    u = math.sqrt(math.pow(lfark,2)+math.pow(wfark,2))
    di.update({i:u})

print(di)
dis = {k: v for k, v in sorted(di.items(), key=lambda item: item[1])}
print(dis)

for i in dis:
    print(sl[i],"  ",sw[i],"  ",i,"  ",tur[i],"  ",dis[i])

dis_list = list(dis)
#print(dis_list)

k_list = []
for i in range(k):
    k_list.append(tur[dis_list[i]])

print(k_list)

versicolor = setosa = virginca = 0
versicolor = k_list.count("Verscicolor")
print(versicolor)

setosa = k_list.count("Setosa")
print(setosa)

virginca = k_list.count("Virginica")
print(virginca)

if versicolor>setosa and versicolor>virginca:
    print("Sınıflandırma sonucu= Verscicolor")
elif setosa>versicolor and setosa>virginca:
    print("Sınıflandırma sonucu= Setosa")
else:
    print("Sınıflandırma sonucu= Virginica")



