import gombákOOP
def gombak():
    lista = []
    fajl = open("gombak.txt", "r", encoding="utf-8")
    adatok = fajl.readlines()
    fajl.close()
    index = 0
    while index < len(adatok):
        helyes = gombákOOP.Gomba(adatok[index])
        lista.append(helyes.gomba)
        index += 1
    print(lista)






