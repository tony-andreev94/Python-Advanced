# https://judge.softuni.bg/Contests/Compete/Index/1837#1

result_list = [f"{each} -> {len(each)}" for each in input().split(", ")]
print(", ".join(result_list))

# no comprehension
words = input().split(", ")
result = []

for each in words:
    each = f"{each} -> {len(each)}"
    result.append(each)

print(", ".join(result))


