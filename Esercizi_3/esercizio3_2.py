import math

class Ellisse():
    def __init__(self, asse_a: float, asse_b: float):
        self._a= math.fabs(asse_a)
        self._b = math.fabs(asse_b)

    def Area(self):
        return math.pi * self._a * self._b

    def Dist_Focale(self):
        return 2*math.sqrt(self._a**2 - self._b**2)

def main():
    asse_a = float(input("Inserisci il valore del semiasse a: "))
    asse_b = float(input("Inserisci il valore del semiasse b: "))

    if asse_a >= asse_b:
        ell = Ellisse(asse_a,asse_b)
        area = ell.Area()
        dist_foc = ell.Dist_Focale()

        print("L'area dell'ellisse e':  %s la distanza focale e': %s " % (area, dist_foc))
    
    else:
        print("Valori non validi")
        
    
if __name__ == "__main__":
    main()
