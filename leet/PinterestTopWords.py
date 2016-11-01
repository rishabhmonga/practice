import json
import urllib
import urllib2
import logging
from collections import Counter

# TODO: Generate access token at https://developers.pinterest.com/tools/access_token/
from collections import defaultdict

logging.basicConfig()
logger = logging.getLogger('PinterestTopWords')

ACCESS_TOKEN = "Ae7rSyQxvaqu32x3KjTNwR4uUjItFIIPTd8anq9Dg79WvSA_XgAAAAA"

BASE_API = "https://api.pinterest.com"

NLTK_STOPWORDS = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had',
                  'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during',
                  'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing',
                  'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't',
                  'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own',
                  'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too',
                  'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he',
                  'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am',
                  'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how',
                  'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the',
                  'having', 'once']


def get_request(path, params=None):
    """
    Given a path, e.g. '/v1/me/' and params, return the response in json form.
    Take a look at https://developers.pinterest.com/docs/getting-started/introduction/
    to see what endpoints the Pinterest API has available!

    You may request additional parameters by overriding the params method
    """
    if params:
        params.update({'access_token': ACCESS_TOKEN})
    else:
        params = {'access_token': ACCESS_TOKEN}
    url = "%s%s?%s" % (BASE_API, path, urllib.urlencode(params))
    result = urllib2.urlopen(url)
    response_data = result.read()
    return json.loads(response_data)


def get_all_board_pins(board_id):
    """
    uses the given board pin to retrieve paginated responses in json form
    """
    cursor = ''
    while cursor is not None:
        try:
            response = get_request('/v1/boards/' + str(board_id) + '/pins/', params={'cursor': cursor})
            cursor = response['page']['cursor']
            for r in response['data']:
                yield r
        except urllib2.URLError as e:
            # not handling the error as behaviour is unknown
            logger.warn("Link Unreachable" + e.message)
            raise e


def get_words_from_note(note):
    """
    retrieves all valid words from a note
    :param note: str
    :return: List[str]
    """
    for word in note.split(' '):
        word = word.lower()
        if is_valid_word(word):
            yield word


def is_valid_word(word):
    """
    validates words
    :param word: str
    :return: bool
    """
    # check if word is part of NLTK_STOPWORDS or is atleast of length 2
    if word in NLTK_STOPWORDS or len(word) < 2:
        return False

    # if the word is made of alphabets it is valid
    if word.isalpha():
        return True

    # check if word starts and ends with an alphabet
    if word[0].isalpha() and word[-1].isalpha():
        for character in word:
            # check if each character is either alphabet or "-" or "'"
            if not character.isalpha() and character != '-' and character != "'":
                return False
        return True
    else:
        return False


def top_n_words(board_id, top_N):
    if top_N is None or top_N < 1 or board_id is None:
        return set()
    pins = get_all_board_pins(board_id)
    words = Counter()
    for pin in pins:
        note = pin['note']
        for w in get_words_from_note(note):
            words[w] += 1

    if len(words) == 0:
        return set()

    # creating a mapping of count -> word
    rev_map = defaultdict(list)
    for word, count in words.most_common():
        rev_map[count].append((word, count))

    result = words.most_common(top_N)

    # get all the elements that match the frequency count of last most common element selected
    last_element = result[-1]
    same_freq_elements = rev_map[last_element[1]]

    # return union of first n result and all remaining elements with same frequency as the last selected result
    return set(words.most_common(top_N)).union(set(same_freq_elements))


if __name__ == '__main__':
    # test cases
    assert is_valid_word("abc") is True
    assert is_valid_word("a-b") is True
    assert is_valid_word("a123") is False
    gen = get_words_from_note("quick brown fox jumped over the lazy dog test123")
    words = ['quick', 'brown', 'fox', 'jumped', 'lazy', 'dog']
    for w1, w2 in zip(gen, words):
        assert w1 == w2
