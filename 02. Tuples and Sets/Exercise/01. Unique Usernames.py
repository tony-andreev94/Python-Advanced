# https://judge.softuni.bg/Contests/Compete/Index/1833#0
# redo and make a return instead of print?


def unique_un(n):
    usernames = []
    for i in range(n):
        username = input()
        usernames.append(username)

    for each in set(usernames):
        print(each)


unique_un(int(input()))
