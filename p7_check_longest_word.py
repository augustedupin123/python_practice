
from inputs import str_input

def check_longest_word(s):
    longest_word = ""
    word_list = s.split()
    for i in range(len(word_list) - 1):
        if len(word_list[i]) > len(word_list[i + 1]):
            longest_word = word_list[i]
        else:
            longest_word = word_list[i + 1]
    return longest_word, len(longest_word)

print(check_longest_word(str_input()))
