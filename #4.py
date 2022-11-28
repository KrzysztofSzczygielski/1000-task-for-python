liczba_uzytkownika = int(input("Wpisz prosze dowolna liczbe dodatnia by otrzymac wszystkie mozliwe jej dzielniki \n"))
b = []

for i in range (1,liczba_uzytkownika):
    if liczba_uzytkownika % i == 0:
        b.append(i)
print (f"dzielnikami liczby {liczba_uzytkownika} sa liczby {b}")
