import math


def get_distance(pt1, pt2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(pt1, pt2)]))


def get_bike_order(locations, biker, bikes):
    preference = []
    for j in range(len(locations)):
        for i in range(len(locations[0])):
            if locations[i][j] in bikes:
                distance = get_distance(biker, (i, j))
                preference.append((locations[i][j], distance))
    return sorted(preference, key=lambda tup: tup[1])


def is_closest(curr, order, taken):
    bikes_with_distance = order[curr]
    for bike, distance in bikes_with_distance:
        if bike not in taken:
            for biker, pref in order.items():
                if biker is not curr:
                    # nearest =
                    pass
            pass
    pass


# def assign_bikes(order, bikers):
#     assigned = {}
#     for biker in bikers:
#         pref = order[biker]
#         for name, distance in pref:
#             if name not in assigned and is_closest(order, ):


def find_bikes(locations, bikers, bikes):
    order = {}
    for j in range(len(locations)):
        for i in range(len(locations[0])):
            if locations[i][j] in bikers:
                order[locations[i][j]] = (get_bike_order(locations, (i, j), bikes))
    print(order)
    # assign_bikes(order, bikers)

    pass


if __name__ == '__main__':
    mat_in = [['A', '*', '*', '*', 'a'],
              ['*', '*', 'b', 'B', '*'],
              ['*', '*', '*', '*', '*'],
              ['c', '*', 'C', '*', '*'],
              ['*', 'D', '*', 'd', '*']]
    bikers = {'A', 'B', 'C', 'D'}
    bikes = {'a', 'b', 'c', 'd'}
    # find_bikes(mat_in, bikers, bikes)
    order = {'A': [('b', 2.23606797749979), ('c', 3.0), ('a', 4.0), ('d', 5.0)], 'D': [('c', 1.4142135623730951), ('d', 2.0), ('b', 3.1622776601683795), ('a', 5.0)], 'C': [('d', 1.4142135623730951), ('c', 2.0), ('b', 2.0), ('a', 3.605551275463989)], 'B': [('b', 1.0), ('a', 1.4142135623730951), ('d', 3.0), ('c', 3.605551275463989)]}
    print(is_closest(order, 'A'))


