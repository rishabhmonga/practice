class obj():
    def __init__(self, prop1, prop2, prop3):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3

    def __eq__(self, other):
        return True if self.prop1 == other.prop1 or self.prop2 == other.prop2 or self.prop3 == other.prop3 else False


def match_properties(a, b):
    return a == b


if __name__ == '__main__':
    obj1 = obj(2, 2, 3)
    obj2 = obj(2, 4, 6)

    print(match_properties(obj1, obj2))