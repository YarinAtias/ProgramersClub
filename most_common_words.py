import re

def remove_non_letters(word):
    return re.sub(r'[^a-zA-Z]', '', word)

def print_most_common_words(file: str, N=None) -> None:
    with open(file, 'r') as f:
        file_to_read = f.read()

    list_of_word = [remove_non_letters(word.strip()) for word in file_to_read.split(" ") if word != "" and len(word) > 1]
    words_counter_dic = {word: list_of_word.count(word) for word in list_of_word}
    words_counter_dic.pop("")
    words_counter_dic = sorted(words_counter_dic.items(), key=lambda item: item[1], reverse=True)

    for i, item in enumerate(words_counter_dic):
        if i == N:
            break
        try:
            print(f"{i + 1} - Word '{item[0]}' {item[1]} times")
        except IndexError:
            break

