# https://judge.softuni.bg/Contests/Practice/Index/1838#8


def get_info(**kwargs):
    return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"


def get_info2(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
print(get_info2(**{"name": "George", "town": "Sofia", "age": 20}))
