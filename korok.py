import random


def korok():
    lista = []





    def elso_idos():
        index = 0
        kor = 70
        (hanyadik) = 0
        while index < len(lista):
            hanyadik += 1
            if lista[index] > kor:
                keresett = hanyadik
                index = len(lista)
            index += 1
        return hanyadik

    def konzolra_ir():
        hanyadik = elso_idos()
        print("II/D, E:")
        print(f"\tElső idős ember korának helye a listában: {hanyadik}")

    def fajl_ir():
        hanyadik = elso_idos()
        fajl = open("oreg.txt", "w", encoding="utf-8")
        fajl.write(f"II/F:\n\tElső idős ember korának helye a listában: {hanyadik}")

        fajl.close()



    print("II/A, B, C:\n\t", end="")
    index = 0
    while index < 5:
        szam = random.randrange(0, 121)
        lista.append(szam)
        index += 1
    index = 0
    while index < len(lista) - 1:
        print(lista[index], end=" : ")
        index += 1
    print(lista[index])
    konzolra_ir()
    fajl_ir()

















