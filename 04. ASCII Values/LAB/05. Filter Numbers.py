# https://judge.softuni.bg/Contests/Practice/Index/1836#4

range_lower = int(input())
range_upper = int(input())

print([x for x in range(range_lower, range_upper + 1) if any([x % d == 0 for d in range(2, 11)])])

# no comprehension
divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for num in range(range_lower, range_upper + 1):
    for divisor in divisors:
        if num % divisor == 0 and num not in result:
            result.append(num)

print(result)




