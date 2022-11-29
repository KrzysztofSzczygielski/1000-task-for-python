# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

first_string = str(input("Wprowadź dowolny wyraz znak \n"))
second_string = first_string.lower().replace(" ","")
second_string_len = len(second_string)
variable_list = []

for i in range (second_string_len-1):
    if second_string[i] != second_string[second_string_len-1-i]:
        variable_list.append(0)
    else:
        variable_list.append(1)
if 0 in variable_list:
    print("Zmienna nie jest palindromem")
else:
    print("Zmienna jest palindromem")
