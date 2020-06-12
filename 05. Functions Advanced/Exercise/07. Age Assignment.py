# https://judge.softuni.bg/Contests/Compete/Index/1839#6


def age_assignment(*args, **kwargs):
    result = {}
    for key, value in kwargs.items():
        for person in args:
            if key == person[0]:
                result[person] = value

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
