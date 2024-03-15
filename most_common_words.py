def print_most_common_words(file: str, N) -> None:
    with open(file, 'r') as f:
        file_to_read = f.read()

    list_of_word = [word.strip() for word in file_to_read.split(" ") if word != ""]
    words_counter_dic = {word: list_of_word.count(word) for word in list_of_word}
    words_counter_dic = sorted(words_counter_dic.items(), key=lambda item: item[1], reverse=True)

    for i, item in enumerate(words_counter_dic):
        if i == N:
            break

        try:
            print(f"{i + 1} - Word '{item[0]}' {item[1]} times ")
        except IndexError:
            break


my_file = "keylogger"
print_most_common_words(my_file, 1)
