def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


if __name__ == '__main__':
    print(judgeCircle("UD"))

