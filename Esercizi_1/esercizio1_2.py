anno = int(input("Inserirsci un anno, inserisci 0 per terminare:"))

while anno != 0:
    if anno % 4 == 0 and anno % 100 != 0 or anno % 400 == 0:
        print(anno,"e' un anno bisestile")
    else:
        print(anno,"non e' un anno bisestile")

    anno = int(input("Inserisci un anno, inserisci 0 per terminare:"))

