# Lab 01 – Zadanie 2 (★): Wizytówka
#
# Program pyta użytkownika kolejno o:
#   1. imię,
#   2. nazwisko,
#   3. rok urodzenia (liczba całkowita),
# a potem wypisuje jedno zdanie, np.:
#     Nazywam się Anna Kowalska i w 2026 roku kończę 20 lat.
#
# Wskazówki:
#   - input() zawsze zwraca tekst (str) – rok zamień na liczbę: int(...)
#   - użyj f-stringa: f"Nazywam się {first_name} ..."

CURRENT_YEAR = 2026

# TODO: Twój kod poniżej

name :str = input("Podaj imię: ")
surname :str = input("Podaj nazwisko: ")
birth_year :int = int(input("Podaj rok urodzenia: "))

age :int = CURRENT_YEAR - birth_year

print(f"Nazywam się {name} {surname} i w {CURRENT_YEAR} roku kończę {age} lat.")