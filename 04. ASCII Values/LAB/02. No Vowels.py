# https://judge.softuni.bg/Contests/Practice/Index/1836#1

string = input()
vowels = ['a', 'A', 'o', 'O', 'u', 'U', 'e', 'E', 'i', 'I']
formatted_string = [letter for letter in string if letter not in vowels]
print(*formatted_string, sep="")
