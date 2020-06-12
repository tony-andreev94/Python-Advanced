# https://judge.softuni.bg/Contests/Compete/Index/1839#7


def palindrome(word, index=0):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if not word[index] == word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


def palindrome_no_recursion(word, index=0):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
