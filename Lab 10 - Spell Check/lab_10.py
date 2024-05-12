import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
def read_dictionary():
    dictionary_list = []
    with open("dictionary.txt", "r") as file:
        for line in file:
            dictionary_list.append(line.strip().upper())
    return dictionary_list
def linear_search(dictionary_list, key):
    for word in dictionary_list:
        if word == key:
            return True
    return False
def linear_search(dictionary_list, key):
    for word in dictionary_list:
        if word == key:
            return True
    return False
def binary_search(dictionary_list, key):
    low = 0
    high = len(dictionary_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if dictionary_list[mid] < key:
            low = mid + 1
        elif dictionary_list[mid] > key:
            high = mid - 1
        else:
            return True
    return False
def spell_check():
    dictionary_list = read_dictionary()

    # Linear search
    print("--- Linear Search ---")
    line_number = 0
    with open("AliceInWonderLand200.txt", "r") as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if not linear_search(dictionary_list, word.upper()):
                    print(f"Line {line_number} possible misspelled word: {word}")

    # Binary search
    print("--- Binary Search ---")
    line_number = 0
    with open("AliceInWonderLand200.txt", "r") as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if not binary_search(dictionary_list, word.upper()):
                    print(f"Line {line_number} possible misspelled word: {word}")

if __name__ == "__main__":
    spell_check()
