def remove_duplicates(nums):
    visited = set()
    duplicates = list()
    N = len(nums)
    for i in nums:
        if i not in visited:
            visited.add(i)
        else:
            duplicates.append(i)
    for i in duplicates:
        nums.remove(i)
    return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 1]
    print(remove_duplicates(nums))
    print(nums)
