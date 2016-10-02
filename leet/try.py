print('hello world'[::-1])


# depth = 6
# l = [-1 for i in range(depth)]
# print(l)

data = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
mask = [1, -1, 3]
new_data = list()
for row in data:
    flag = False
    for i in range(len(mask)):
        if mask[i] != -1 and mask[i] == row[i]:
            flag = True
    if flag:
        new_data.append(row)

print(new_data)
