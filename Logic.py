import pickle
import random


def get_dict():
    return pickle.load(open("dictionary.p", "rb"))


def generate_substring(dictionary):
    random_word = random.sample(dummy_dict, 1)[0]
    random_num = random.randint(0, len(random_word)-2)
    substring = random_word[random_num: random_num+3]
    return substring


def input_check(dummy_dict, user_input, substring, words_used_list):
    if substring not in user_input:
        print("Invalid input: does not contain string")
        return False
    if user_input not in dummy_dict:
        print("Invalid input: not found in dictionary")
        return False
    if user_input in words_used_list:
        print("Invalid input: word repeated")
        return False
    print("User input valid")
    return True


while True:
    user_input = input("Type a word: ")
    correct_input = input_check(dummy_dict, user_input, substring, words_used_list)
    if correct_input:
        words_used_list.append(user_input)
        break


if __name__ == "__main__":
    words_used_list = []
    dummy_dict = get_dict()
    substring = generate_substring(dummy_dict)
    print(dummy_dict)
    print(substring)