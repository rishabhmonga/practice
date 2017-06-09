import json

if __name__ == '__main__':
    f = open('book.txt', 'r')
    s = f.read()
    book = json.loads(s)
    print(type(book))

    for person in book:
        print(book[person])
