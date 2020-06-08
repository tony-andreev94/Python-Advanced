# https://judge.softuni.bg/Contests/Compete/Index/1837#2

countries = input().split(", ")
capitals = input().split(", ")

zipped = tuple(zip(countries, capitals))
capitals_dict = {zipped[i][0]: zipped[i][1] for i in range(len(zipped))}
for key, value in capitals_dict.items():
    print(f"{key} -> {value}")


# no comprehension
countries = input().split(", ")
capitals = input().split(", ")

my_dict = {}
for i in range(len(countries)):
    my_dict[countries[i]] = capitals[i]
for key, value in my_dict.items():
    print(f"{key} -> {value}")
