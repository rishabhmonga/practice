def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    vocab = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morseRepresentation = set()
    begin = 97
    for word in words:
        rep = ''
        for c in word:
            rep += vocab[ord(c) - begin]
        morseRepresentation.add(rep)
    return len(morseRepresentation)




if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    print(uniqueMorseRepresentations(words))
