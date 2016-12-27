def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    result = [0, 0]
    secret_list = list(secret)
    guess_list = list(guess)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result[0] += 1
            secret_list[i] = ''
            guess_list[i] = ' '
    for i in range(len(guess_list)):
        if guess_list[i] in secret_list:
            result[1] += 1
            secret_list[secret_list.index(guess_list[i])] = ''
            guess_list[i] = ' '
    return str(result[0]) + 'A' + str(result[1]) + "B"

if __name__ == '__main__':
    # print(getHint('1234', '4321'))
    print(getHint('11', '10'))
    # print(getHint('1234', '0111'))
    # print(getHint('011', '110'))
