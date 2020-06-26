# Task 1

file_path = 'W:\\Documents\\@Python\\SoftUni\\python_advanced\\06_file_handling\\08-File-Handling-Lab-Resources\\Words Count\\text.txt'


def replace_symbols(text):
    symbols = ["-", ",", ".", "!", "?"]
    for each_character in text:
        for each_symbol in symbols:
            if each_character == each_symbol:
                char_index = text.index(each_character)
                text = text[:char_index] + '@' + text[char_index + 1:]
    return text

index = 0
with open(file_path, 'r') as file:
    even_lines_text = []
    while True:
        line = file.readline().rstrip()
        if line == '':
            break
        if index % 2 == 0:
            # do symbol swapping
            filtered_line = replace_symbols(line)
            even_lines_text.append(filtered_line)
        index += 1

print(even_lines_text)


def reverse_words(words_list):
    result = []
    for each in words_list:
        line = each.split(" ")
        line.reverse()
        result.append(line)
    return result


def print_output(reversed_list):
    for each_el in reversed_list:
        print(end="")
        for each_word in each_el:
            print(each_word, end=" ")


print_output(reverse_words(even_lines_text))



