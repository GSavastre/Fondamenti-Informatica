import math

def sphere_density(raggio: float, massa: float) ->float:
    return massa/((4/3) * math.pi * (raggio **3))
    
def main():
    raggio = float(input("Inserisci il valore del raggio della sfera in metri: "))
    massa = float(input("Inserisci la massa della sfera in Kg: "))
    print("La sfera ha una densità di ",sphere_density(raggio,massa))

if __name__ == "__main__":
    main()
