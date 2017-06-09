import json

book = {'tom': {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 986348943
}, 'bob': {
    'name': 'bob',
    'address': '1 green street NY',
    'phone': 986348943
}}

if __name__ == '__main__':
    s = json.dumps(book)
    print(s)

    with open('./book.txt', 'w') as f:
        f.write(s)
