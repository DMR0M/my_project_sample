"""Create a program that reverses a given input string, and determines if it is a palindrome"""

# Functional Implementation


def reverse_string(word):
    return word[::-1]


def palindrome_string(word):
    lcase_word = word.lower()
    return lcase_word == lcase_word[::-1]


# user_string = input('Input text to reverse: ')
# print(reverse_string(user_string))
# print(palindrome_string(user_string))


# OOP Implementation

class CheckString:
    def __init__(self, word):
        self.word = word

    def reverse_word(self):
        return self.word[::-1]

    def check_if_palindrome(self):
        lcase_word = self.word.lower()
        return lcase_word == lcase_word[::-1]


if __name__ == '__main__':
    user_text = input('Input text to check: ')
    user_1 = CheckString(user_text)
    reversed_string: str = user_1.reverse_word()
    is_palindrome: bool = user_1.check_if_palindrome()
    ans_dict = {reversed_string: is_palindrome}
    print(ans_dict)
