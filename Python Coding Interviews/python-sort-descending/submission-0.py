from typing import List


def sort_words(word_list):
    word_list.sort(reverse=True)
    return word_list 

def sort_numbers(numbers_list):
    numbers_list.sort(reverse=True)
    return numbers_list

def sort_decimals(decimals_list):
    decimals_list.sort(reverse=True)
    return decimals_list


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
