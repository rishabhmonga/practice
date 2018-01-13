def isCompound(data, word, iterations=0):
    if not data or not word or word is '':
        return False
    for w in data:
        if w == word and iterations > 0:
            return True
        if w == word[0: len(w) - 1]:
            subWord = word[len(w):]
            if isCompound(data, subWord, iterations + 1):
                return True
    return False


def get_simple_words(data):
    result = []
    for w in data:
        if not isCompound(data, w):
            result.append(w)

    return result


if __name__ == '__main__':
    data = ['sales', 'person', 'salesperson']
    print(get_simple_words(data))
