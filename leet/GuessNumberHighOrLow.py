class GuessGame:
    def __init__(self, x):
        self.x = x

    def guess(self, num):
        if num == self.x:
            return 0
        elif num < self.x:
            return -1
        else:
            return 1

    def guessNumber(self, n):
        if n == 1:
            return n
        if self.guess(n) == 0:
            return n
        if self.guess(n) > 0:
            return self.guessNumber(int(n/2))
        if self.guess(n) < 0:
            return self.guessNumber(int(3*n/2))


if __name__ == '__main__':
    soln = GuessGame(6)
    print(soln.guessNumber(10))
