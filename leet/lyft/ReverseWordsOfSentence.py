def reverseWords(s):
    word_stack = []
    s = s.split(' ')
    for w in s:
        if w != '':
            word_stack.append(w)
    res = ''
    while word_stack:
        word = word_stack.pop()
        res += word
        if word_stack:
            res += ' '
    return res


def reverseWords2(s):
    return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    print(reverseWords2('the sky is blue'))
    assert (reverseWords2(' 1') == '1'), 'fail'
