# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
bok1 :float = float(input("Podaj długość pierwszego boku: "))
bok2 :float = float(input("Podaj długość drugiego boku: "))
bok3 :float = float(input("Podaj długość trzeciego boku: "))
if (bok1 + bok2 <= bok3) or (bok1 + bok3 <= bok2) or (bok2 + bok3 <= bok1):
    print("Nie da się zbudować trójkąta")  
elif bok1 == bok2 == bok3:
    print("Trójkąt równoboczny")
elif bok1 == bok2 or bok1 == bok3 or bok2 == bok3:
    print("Trójkąt równoramienny")
elif bok1 != bok2 and bok1 != bok3 and bok2 != bok3:
    print("Trójkąt różnoboczny")
if abs(bok1**2 + bok2**2 - bok3**2) < 1e-9 or abs(bok1**2 + bok3**2 - bok2**2) < 1e-9 or abs(bok2**2 + bok3**2 - bok1**2) < 1e-9:
    print("Trójkąt prostokątny")