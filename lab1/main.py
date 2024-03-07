import math


def cerinta1():
    '''
    Complexitate timp O(n*logn)
    Complexitate spatiu O(n*m) = O(n^2), unde n este nr de char din string si m nr de stringuri
    :ce face: citeste o propozitie si gaseste ultimul cuvant alfabetic
    '''
    text = input("Propozitie: ")
    cuvinte = text.split()
    lista = [(cuv, cuv.lower()) for cuv in cuvinte]
    lista.sort(key=lambda x: x[1], reverse=True)
    print(f"Ultimul cuvant alfabetic din propozitie e '{lista[0][0]}'")

def cerinta1_gpt():
    text = input("Propozitie: ")
    cuvinte = text.split()  # Descompune textul într-o listă de cuvinte
    return max(cuvinte)  # Găsește cuvântul cu valoarea cea mai mare din punct de vedere alfabetic


def cerinta2():
    '''
    Complexitate timp O(1)
    Complexitate spatiu O(1) nu se folosesc arrays
    :ce face: citeste x, y pentru doua locatii si calculeaza distanta euclideana dintre ele
    '''
    x1, y1 = input("Prima locatie (x y): ").split()
    x2, y2 = input("A doua locatie (x y): ").split()
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    distanta = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    print(f"Distanta de la ({x1}, {y1}) la ({x2}, {y2}) este {distanta}")

def distanta_euclidiana_gpt(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def creinta2_gpt():
    p1 = tuple(map(float, input("Introduceti coordonatele primului punct (x1, y1): ").split()))
    p2 = tuple(map(float, input("Introduceti coordonatele celui de-al doilea punct (x2, y2): ").split()))
    distanta = distanta_euclidiana_gpt(p1, p2)
    print("Distanța Euclideană între", p1, "și", p2, "este:", distanta)


def cerinta4():
    '''
    Complexitate timp O(n)
    Complexitate spatiu O(n*m) = O(n^2), unde n este nr de char din string si m nr de stringuri
    :ce face: citeste o propozitie si gaseste cuvintele unice
    '''
    frecventa = {}
    _input = input("Propozitie: ")
    cuvinte = _input.split()
    for cuv in cuvinte:
        if cuv in frecventa:
            frecventa[cuv] += 1
        else:
            frecventa[cuv] = 1
    cuvinte_unice = [cuv for cuv, value in frecventa.items() if value == 1]
    print(f"Cuvintele sunt: {cuvinte_unice}")


def cerinta4_gpt():

    text = input("Propozitie: ")
    # Inițializăm un dicționar gol pentru a număra de câte ori apare fiecare cuvânt
    frecventa_cuvinte = {}

    # Descompunem textul în cuvinte
    cuvinte = text.split()

    # Iterăm prin fiecare cuvânt și actualizăm frecvența în dicționar
    for cuvant in cuvinte:
        frecventa_cuvinte[cuvant] = frecventa_cuvinte.get(cuvant, 0) + 1

    # Selectăm cuvintele care apar o singură dată
    cuvinte_unice = [cuvant for cuvant, frecventa in frecventa_cuvinte.items() if frecventa == 1]

    print(cuvinte_unice)


def cerinta5():
    '''
    Complexitate timp O(n*logn)
    Complexitate spatiu O(n), unde n este nr de numere
    :ce face: citeste un sir de numere in care unul e duplicat si il gaseste
    '''
    _input = input("Sir de numere: ")
    elems = []
    for el in _input.split():
        x = int(el)
        elems.append(x)
    elems.sort()
    n = len(elems) - 1
    while n > 0:
        if elems[n] == elems[n-1]:
            print(f"{elems[n]} este elementul duplicat")
            return
        n -= 1


def cerinta5_gpt(arr):
    frecventa_valori = {}

    for valoare in arr:
        frecventa_valori[valoare] = frecventa_valori.get(valoare, 0) + 1

    for valoare, frecventa in frecventa_valori.items():
        if frecventa == 2:
            print(valoare)


def cerinta7():
    '''
    Complexitate timp O(n*logn)
    Complexitate spatiu O(n), unde n este nr de numere
    :ce face: citeste un sir de numere si gaseste al k cel mai mare nr de la cel mai mare la cel mai mic
    '''
    _input = input("Sir de numere: ")
    k = int(input("Spune al catelea cel mai mare elem il vrei, k = "))
    elems = []
    for el in _input.split():
        elems.append(int(el))
    elems.sort(reverse=True)
    print(f"{elems[k - 1]}")


def cerinta7_gpt():
    n = int(input("Introduceti lungimea sirului: "))
    sir = list(map(int, input("Introduceti sirul de numere separate prin spatii: ").split()))
    k = int(input("Introduceti valoarea lui k: "))

    if k >= n:
        print("Eroare: k trebuie să fie mai mic decât lungimea sirului.")
        return

    sir_sortat = sorted(sir, reverse=True)
    result = sir_sortat[k - 1]
    print(f"Al {k}-lea cel mai mare element din șirul {sir} este:", result)


def iesire():
    print("Iesire din program.")
    quit()


# Meniu
print("=== MENIU ===")
print("1. Cerinta 1")
print("2. Cerinta 2")
print("3. Cerinta 4")
print("4. Cerinta 5")
print("5. Cerinta 7")
print("6. Exit")


while True:
    optiune = input("Selectati o optiune: ")

    if optiune == '1':
        cerinta1()
    elif optiune == '2':
        cerinta2()
    elif optiune == '3':
        cerinta4()
    elif optiune == '4':
        cerinta5()
    elif optiune == '5':
        cerinta7()
    elif optiune == '6':
        iesire()
    else:
        print("Optiune invalida. Va rugam selectati o optiune valida.")
