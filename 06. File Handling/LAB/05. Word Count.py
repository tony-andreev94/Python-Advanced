# Task 5

words_path = 'W:\\Documents\\@Python\\SoftUni\\python_advanced\\06_file_handling\\08-File-Handling-Lab-Resources\\Words Count\\words.txt'
text_path = 'W:\\Documents\\@Python\\SoftUni\\python_advanced\\06_file_handling\\08-File-Handling-Lab-Resources\\Words Count\\text.txt'


def extract_words(file_path):
    with open(file_path, 'r') as words_file:
        words_list = words_file.readline().split(" ")
    return words_list


def count_words_in_text(words, text):
    words_dict = {word: 0 for word in words}
    with open(text, 'r') as text_file:
        while True:
            line = text_file.readline().lower()
            if line == '':
                break
            else:
                for each_word in words:
                    if each_word in line:
                        words_dict[each_word] += 1
        return words_dict


def print_formatted_dict(dict):
    sorted_dict = sorted(dict.items(), key= lambda pair: (-pair[1], pair[0]))
    [print(f"{word} - {count}") for word, count in sorted_dict]


words = extract_words(words_path)
words_dict = count_words_in_text(words, text_path)
print_formatted_dict(words_dict)
