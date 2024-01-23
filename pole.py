def oblicz_pole_prostokata(dlugosc, szerokosc):
    return dlugosc * szerokosc

dlugosc = float(input("Podaj długość boku prostokąta: "))
szerokosc = float(input("Podaj szerokość boku prostokąta: "))

pole = oblicz_pole_prostokata(dlugosc, szerokosc)
print(f"Pole prostokąta o bokach {dlugosc} i {szerokosc} wynosi: {pole}")
