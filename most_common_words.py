import re
import sys

# Gets a string and returns the same string without punctuations
def remove_non_letters(word):
    return re.sub(r'[^a-zA-Z]', '', word)

def print_most_common_words(file: str, N=None) -> None:
    # File handling
    try:
        with open(file, 'r') as f:
            file_to_read = f.read()
    except:
        file_to_read = file

    # Creates a dictionary of file's words and as the key and the occurrences number for each word
    list_of_word = [remove_non_letters(word.strip()) for word in file_to_read.split(" ") if word != "" and len(word) > 1]
    words_counter_dic = {word: list_of_word.count(word) for word in list_of_word}
    try:
        words_counter_dic.pop("")
    except:
        pass
    words_counter_dic = sorted(words_counter_dic.items(), key=lambda item: item[1], reverse=True)

    # Prints the N most common words
    for i, item in enumerate(words_counter_dic):
        if i == N:
            break
        try:
            print(f"{i + 1} - Word '{item[0]}' {item[1]} times")
        except IndexError:
            break


def main():
    file_content = sys.argv[1]
    N_WORDS_TO_SHOW = int(sys.argv[2])
    print_most_common_words(file_content, N_WORDS_TO_SHOW)


if __name__ == "__main__":
    main()
