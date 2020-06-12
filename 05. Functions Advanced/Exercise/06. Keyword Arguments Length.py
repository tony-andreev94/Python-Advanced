# https://judge.softuni.bg/Contests/Compete/Index/1839#5


def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
