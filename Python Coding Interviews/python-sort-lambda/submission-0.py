from typing import List

def get_word_length(s: str) -> int:
    return len(s)

def get_abs(num: int) -> int:
    return abs(num)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda s: len(s), reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda abs_val: abs(abs_val))
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
