# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
import datetime
dzis=datetime.date.today()
imie = input ("Podaj swoje imie\n")
rok = int(input ("Podaj rok swojego urodzenia\n"))
wiek = int(dzis.strftime("%Y"))- rok
wiek100 = (rok + 100)

if wiek >100:
    print("Ha ha ha bardzo śmieszne ludzie tyle nie żyją")
elif wiek < 0:
    print("Chyba jeszcze się nie narodziłeś musimy poczekać")
elif wiek == 0:
    print(f"Podziwiam cie {imie} w wieku {wiek} lat już umiesz pisać, sto lat osiągniesz w {wiek100} roku")
elif wiek == 1:
    print(f"Podziwiam cie {imie} że w wieku {wiek} roku już umiesz pisać, sto lat osiągniesz w {wiek100} roku")
elif wiek >= 2 and wiek < 5:
    print(f"Podziwiam cie {imie} że w wieku {wiek} lat już umiesz pisać, sto lat osiągniesz w {wiek100} roku")
else:
    print(f"Cześć {imie} widzę że masz {wiek} lat, sto lat osiągniesz w {wiek100} roku")
