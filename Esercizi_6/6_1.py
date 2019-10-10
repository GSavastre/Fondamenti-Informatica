class Person():
    def __init__(self, nome: str, cognome: str, giorno_n: int, mese_n: int, anno_n: int):
        self._nome = nome
        self._cognome = cognome
        self._giorno = giorno_n
        self._mese = mese_n
        self._anno = anno_n

    def Name(self):
        return self._nome

    def Age(self,questo_giorno:int, questo_mese: int, questo_anno: int):

        anno = questo_anno - self._anno    

        if questo_anno <= self._anno:
            return 0
        elif anno > 0 and questo_mese < self._mese:
            return anno - 1
        else:
            return anno
            

def main():
    nome = str(input("Inserisci il nome: "))
    cognome = str(input("Inserisci il  cognome: "))
    nascita = str(input("Inserisci la tua data di nascita (GG/MM/AAAA): "))

    giorno, mese, anno = nascita .split("/")

    persona = Person(nome, cognome, int(giorno), int(mese), int(anno))

    #giorno_presente, mese_presente etc...

    giorno_p, mese_p, anno_p = str(input("Inserisci la data corrente(GG/MM/AAAA): ")).split("/")

    eta = persona.Age(int(giorno_p), int(mese_p), int(anno_p))
    
    print(persona.Name()," ha ", int(eta)," anni")

if __name__ == "__main__":
    main()
