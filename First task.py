import math

def is_prime_number(check_number: int) -> bool:
    prime = True
    for number in range(2, int(math.sqrt(check_number)) + 1):
        if (check_number % number) == 0:
            prime = False
    return prime


def prime_numbers_in_range(minimum, maximum: int) -> list:
    prime_numbers_list = []
    for number in range(minimum, maximum + 1):
        if is_prime_number(number):
            prime_numbers_list.append(number)
    return prime_numbers_list


def reverse_string():
    user_input = input("Insert your input: ")
    new_string = ""
    for letter in user_input:
        new_string = letter + new_string
    print(f"The new string is {new_string}")


def is_string_palindrome(text: str) -> bool:
    is_palindrome = True
    for index in range(len(text) // 2):
        if text[index] != text[len(text) - index - 1]:
            is_palindrome = False
    return is_palindrome


def longest_word_in_sentence(sentence: str):
    list_of_words = sentence.split(" ")
    word = max(list_of_words, key=len)
    return word

def find_missing_number(main_list: list):
    list_sum = 0
    list_length = len(main_list)
    total_sum = (list_length + 1) * (list_length + 2) / 2

    for number in main_list:
        list_sum = list_sum + number

    missing_number = int(total_sum - list_sum)
    return missing_number


# my_list = [4, 2, 5, 7, 1, 3, 8, 10, 9]
# print(find_missing_number(my_list))
