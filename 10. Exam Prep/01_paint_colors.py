# https://judge.softuni.bg/Contests/Practice/Index/2306#0

input_str = input().split()

main_colors = ['red', 'yellow', 'blue']
sec_colors = {'orange': ['red', 'yellow'],
              'purple': ['red', 'blue'],
              'green': ['yellow', 'blue']
              }
results = []

while input_str:
    first = input_str.pop(0)
    last = ""
    if len(input_str) != 0:
        last = input_str.pop()
    first_comb = first + last
    second_comb = last + first
    if first_comb in main_colors or first_comb in sec_colors:
        results.append(first_comb)
    elif second_comb in main_colors or second_comb in sec_colors:
        results.append(second_comb)
    else:
        index = len(input_str) // 2
        if not first[:-1] == "":
            input_str.insert(index, first[:-1])
        if not last[:-1] == "":
            input_str.insert(index, last[:-1])

for each in results:
    if each in sec_colors.keys():
        if not sec_colors[each][0] in results or sec_colors[each][1] not in results:
            results.remove(each)

print(results)
