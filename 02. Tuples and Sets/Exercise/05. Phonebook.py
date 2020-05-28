# https://judge.softuni.bg/Contests/Compete/Index/1833#4
# redo and use new material


def phonebook():
    phone_dict = {}
    while True:
        user_input = input()
        if len(user_input) > 1:
            data = user_input.split("-")
            phone_dict[data[0]] = data[1]
        else:
            queries = int(user_input)
            break

    for i in range(queries):
        query_name = input()
        if query_name in phone_dict.keys():
            print(f"{query_name} -> {phone_dict[query_name]}")
        else:
            print(f"Contact {query_name} does not exist.")


phonebook()
