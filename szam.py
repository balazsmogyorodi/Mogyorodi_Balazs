def szam():
    print("I/A:")
    egySzam = 0
    while egySzam < 1 or egySzam > 50:
        egySzam = int(input("\tA generált szám: "))
    print("I/B:")
    if (egySzam % 3 == 0) and (egySzam % 5 == 0):
        print("\tA szám öttel és hárommal is osztható!")
    elif egySzam % 3 == 0:
        print("\tA szám hárommal  osztható!")
    elif egySzam % 5 == 0:
        print("\tA szám öttel osztható!")






