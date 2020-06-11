# https://judge.softuni.bg/Contests/Compete/Index/1837#0

print("\n".join([word for word in input().split() if len(word) % 2 == 0]))

# no comprehension
words = input().split()

for each_word in words:
    if len(each_word) % 2 == 0:
        print(each_word)
