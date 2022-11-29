# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#  napisz program który zwróci listę zawierającą tylko elementy które są wspólne dla obu list (nie zduplikowane). Upewnij się że twój program działa dla dwóch list z zmienną wielkością.
# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
uniqueList_A = []

for elem in a:
    if elem not in uniqueList_A:
        uniqueList_A.append(elem)

print(f"Unikalna wartość dla A{uniqueList_A}")
        
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
uniqueList_B = []

for elem in a:
    if elem not in uniqueList_B:
        uniqueList_B.append(elem)

print(f"Unikalna wartość dla A{uniqueList_B}")

c = []
d = []

for i in range (len(uniqueList_A )):
    if uniqueList_A [i] in uniqueList_B:
        c.append(uniqueList_A [i])

for i in range (len(uniqueList_B)):
    if uniqueList_B[i] in uniqueList_A:
        d.append(uniqueList_B[i])  
print(c)
print(d)       

# 2

# Generowanie liczb losowych oraz wyodrębnianie z nich unikalnej wartości
from random import randrange
random_number_list = [randrange(1,10) for i in range(10)]
uniqueList_random_number_list = []

for elem in random_number_list:
    if elem not in uniqueList_random_number_list:
        uniqueList_random_number_list.append(elem)

random_number_list2 = [randrange(1,10) for i in range(10)]
uniqueList_random_number_list2=[]

for elem in random_number_list2:
    if elem not in uniqueList_random_number_list2:
        uniqueList_random_number_list2.append(elem)

print(f"unikalne wartości losowych liczb \n{uniqueList_random_number_list}")
print(f"unikalne wartości losowych liczb2 \n{uniqueList_random_number_list2}")
common_number_list = []
common_number_list2 = []

# Wyodrębnianie części wspólnych
for i in range (len(uniqueList_random_number_list)):
    if uniqueList_random_number_list[i] in uniqueList_random_number_list2:
        common_number_list.append(uniqueList_random_number_list[i])

for i in range (len(uniqueList_random_number_list2)):
    if uniqueList_random_number_list2[i] in uniqueList_random_number_list:
        common_number_list2.append(uniqueList_random_number_list2[i])  

print (f"cześci wspólne losowych liczb \n{common_number_list}")
print (f"cześci wspólne losowych liczb \n{common_number_list2}")



