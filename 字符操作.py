__author__ = 'barryclass'

# 从字符中提取子串包含的字符

import itertools
import string


def make_filter(keep):
    all_characters = string.maketrans('', '')
    print(all_characters)

    delete_characters = all_characters.translate(all_characters, keep)
    print(delete_characters)

    def the_filter(s):
        return s.translate(all_characters, delete_characters)
    return the_filter

if __name__ == '__main__':
    just_vowels = make_filter('aeiou')
    print(just_vowels('four score and seven years ago'))