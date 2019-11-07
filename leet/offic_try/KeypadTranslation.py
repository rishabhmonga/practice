keypad = {'2': ['a', 'b', 'c'],
          '3': ['d', 'e', 'f'],
          '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'],
          '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'],
          '9': ['w', 'x', 'y', 'z']
          }


def words_4_number(number, dictionary):
    possible_words = []
    i = 0
    while i < len(number):
        possible_words = []
        for word in dictionary:
            if len(word) > i and word[i] in keypad[number[i]]:
                possible_words.append(word)
        if len(possible_words) == 0:
            return list()
        i += 1
    return possible_words


if __name__ == '__main__':
    words = ['mother', 'fun', 'freedom', 'father', 'right', 'to', 'fight']

    print(words_4_number('3733366', words))
    print(words_4_number('386', words))
    print(words_4_number('234', words))
