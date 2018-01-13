# class Solution:
#     # @param {character[][]} board
#     # @param {string[]} words
#     # @return {string[]}
#     def findWords(self, board, words):
#         # make trie
#         trie = {}
#         for w in words:
#             t = trie
#             for c in w:
#                 if c not in t:
#                     t[c] = {}
#                 t = t[c]
#             t['#'] = '#'
#         self.res = set()
#         self.used = [[False] * len(board[0]) for _ in range(len(board))]
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.find(board, i, j, trie, '')
#         return list(self.res)
#
#     def find(self, board, i, j, trie, pre):
#         if '#' in trie:
#             self.res.add(pre)
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
#             return
#         if not self.used[i][j] and board[i][j] in trie:
#             self.used[i][j] = True
#             self.find(board, i + 1, j, trie[board[i][j]], pre + board[i][j])
#             self.find(board, i, j + 1, trie[board[i][j]], pre + board[i][j])
#             self.find(board, i - 1, j, trie[board[i][j]], pre + board[i][j])
#             self.find(board, i, j - 1, trie[board[i][j]], pre + board[i][j])
#             self.used[i][j] = False


def check_char(words, board, x, y):
    res = []
    for w in words:
        if board[x][y] == w[0]:
            res.append(w)
    return res


def check_word_recurse(w, board, i, j, x, idx_set):
    if x < len(w):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in idx_set and w[x] == board[i][j]:
            idx_set.add((i, j))
            return check_word_recurse(w, board, i + 1, j, x + 1, idx_set) or check_word_recurse(w, board, i - 1, j, x + 1, idx_set) or check_word_recurse(w, board, i, j + 1, x + 1, idx_set) or check_word_recurse(w, board, i, j - 1, x + 1, idx_set)
        else:
            # if (i, j) in idx_set:
            #     idx_set.remove((i, j))
            return False
    else:
        return True


def check_word(w, board, i, j):
    idx_set = set()
    res = check_word_recurse(w, board, i, j, 0, idx_set)
    return res


def word_search(board, words):
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            w_list = check_char(words, board, i, j)
            for w in w_list:
                if check_word(w, board, i, j):
                    res.append(w)
    return res


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]

    # print(word_search(board, words))

    board = [["a","a"]]
    words = ['aaa']

    # print(word_search(board, words))

    board = [["a", "b"],
             ["c", "d"]]
    words = ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]

    # ["ab","ac","bd","ca","db"]
    # print(word_search(board, words))

    board = [["a", "b", "c"],
             ["a", "e", "d"],
             ["a", "f", "g"]]
    words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]

    print(check_char(words, board, 1, 1))
    print(check_word('eaabcdgfa', board, 1, 1))
