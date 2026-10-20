# Lab 03 – Zadanie 3 (★): Rok przestępny
#
# Rok jest przestępny, gdy:
#   - dzieli się przez 4 i NIE dzieli się przez 100,
#   - albo dzieli się przez 400.
#
# Wypisz dokładnie jedno z dwóch zdań:
#     Rok 2024 jest przestępny
#     Rok 2023 nie jest przestępny
#
# Wskazówka: warunek zapiszesz w jednej linii z and / or.

# TODO: Twój kod poniżej
rok :int=2024
rok2 :int=2023
if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print(f"Rok {rok} jest przestępny")
else:
    print(f"Rok {rok} nie jest przestępny")

if (rok2 % 4 == 0 and rok2 % 100 != 0) or rok2 % 400 == 0:
    print(f"Rok {rok2} jest przestępny")
else:
    print(f"Rok {rok2} nie jest przestępny")    