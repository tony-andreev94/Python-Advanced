# https://judge.softuni.bg/Contests/Practice/Index/1832#1


def grade_average(grades):
    grade_dict = {}
    for _ in range(grades):
        user_input = input().split(" ")
        student = user_input[0]
        grade = user_input[1]
        if student not in grade_dict.keys():
            grade_dict[student] = [float(grade)]
        else:
            grade_dict[student].append(float(grade))

    return grade_dict


def print_grades(grade_dict):
    for (student, grade) in grade_dict.items():
        avg_grade = sum(grade) / len(grade)
        grades_string = ' '.join(f'{x:.2f}' for x in grade)
        print(f"{student} -> {grades_string} (avg: {avg_grade:.2f})")


grades = int(input())
print_grades(grade_average(grades))
