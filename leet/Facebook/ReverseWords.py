def reverse_words(sentence):
    curr_str = ''
    ans = ''
    for i in range(len(sentence) - 1, -1, -1):
        if sentence[i] != ' ':
            curr_str += sentence[i]
        if sentence[i] == ' ' or i == 0:
            ans += curr_str[::-1]
            ans += ' '
            curr_str = ''
    return ans



if __name__ == '__main__':
    sentence = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
    print(reverse_words(sentence))
