## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

# [i, like, dogs, ilike]
# "ilikedogs"
# => "i like dogs"
# => "ilike dogs"

# i
# /     \
# ' '   l
# /


# if trie.child is in dict:
#     if trie.child.length() == len(s):
#         return
#     if trie.child = s[i]

# found =
# i like dogs

memo = dict()
indexes = [0]


def find_words(s, dictionary, idx):
    if s in dictionary:
        if s not in memo:
            memo[idx] = s

        return True

    chars = ''
    for i in range(len(s)):
        chars += s[i]
        if chars in dictionary:
            if idx not in memo:
                memo[idx] = chars
            if find_words(s[i + 1:], dictionary, i + 1):
                indexes.append(i)
                break

    return False


find_words("ilikedogs", ['i', 'like', 'dogs', 'ilike'], 0)
print(memo)
print(indexes)