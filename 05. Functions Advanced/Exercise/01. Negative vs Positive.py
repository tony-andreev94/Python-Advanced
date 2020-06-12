# https://judge.softuni.bg/Contests/Compete/Index/1839#0


def numbers(values):
    positive_sum = sum([x for x in values if x >= 0])
    negative_sum = sum([x for x in values if x < 0])
    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


values_list = [int(x) for x in input().split()]
print(numbers(values_list))
