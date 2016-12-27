def is_compound_word(word, vocabulary, depth=0):
    if len(vocabulary) < 1:
        return False
    if len(word) < 1:
        return False

    # word_partition[i] will be True if substring of word[0:i-1] is in my vocabulary
    word_partition = [False for _ in range(len(word) + 1)]
    for i in range(1, len(word)):
        # current substring is word[0:i]


        # if the current substring if not set in the word_partition map,
        # then check if it is present in the vocabulary
        if word_partition[i] is False and word[0:i] in vocabulary:
            word_partition[i] = True

        # if it is present in the vocabulary then check for all substrings starting from
        # the (i+1)th character and set results in the word_partition
        if word_partition[i] is True:
            # checking the last prefix
            if i == len(word):
                return True
            for j in range(i + 1, len(word) + 1):
                # similarly if the substring [i:j] is not set in the word_partition,
                # then check if it is part of vocabulary
                if word_partition[j] is False and word[i:j] in vocabulary:
                    word_partition[j] = True
                # since we reached the end of the word and substring part of vocabulary
                # we can return True
                if j == len(word) and word_partition[j] is True:
                    return True
    return False


def simpleWords(words):
    if words is None:
        return None
    if len(words) < 1:
        return []

    simple_words = []
    vocab = set(words)
    for word in words:
        if not is_compound_word(word, vocab):
            simple_words.append(word)
    return simple_words
