# https://judge.softuni.bg/Contests/Compete/Index/1837#3

numbers = [int(x) for x in input().split(", ")]

positive = [str(x) for x in numbers if x >= 0]
negative = [str(x) for x in numbers if x < 0]
even = [str(x) for x in numbers if x % 2 == 0]
odd = [str(x) for x in numbers if not x % 2 == 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")


# no comprehension
numbers = [int(x) for x in input().split(", ")]

positive = []
negative = []
even = []
odd = []

for each in numbers:
    if each >= 0:
        positive.append(each)
    if each < 0:
        negative.append(each)
    if each % 2 == 0:
        even.append(each)
    if not each % 2 == 0:
        odd.append(each)

print(f"Positive: {', '.join([str(x) for x in positive])}")
print(f"Negative: {', '.join([str(x) for x in negative])}")
print(f"Even: {', '.join([str(x) for x in even])}")
print(f"Odd: {', '.join([str(x) for x in odd])}")
