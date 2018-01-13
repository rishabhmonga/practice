from collections import Counter


def get_execution_time(tasks, k):
    if not tasks:
        return 0
    count = 1
    for idx in range(1, len(tasks)):
        count += 1
        if tasks[idx] == tasks[idx - 1]:
            count += k
    return count


def optimize_sequence(tasks, k):
    if get_execution_time(tasks, k) == len(tasks):
        return tasks
    ans = ''
    task_count = Counter(tasks).most_common()
    while task_count:
        if task_count:
            if task_count[0][1] > 0:
                ans += task_count[0][0]
                task_count[0] = (task_count[0][0], task_count[0][1] - 1)
                print(ans, task_count)
            else:
                task_count.pop()
                if task_count:
                    ans += task_count[0][0]
                    task_count[0] = (task_count[0][0], task_count[0][1] - 1)
                    print(ans, task_count)

        if task_count:
            if task_count[-1][1] > 0:
                ans += task_count[-1][0]
                task_count[-1] = (task_count[-1][0], task_count[-1][1] - 1)
                print(ans, task_count)
            else:
                task_count.pop(-1)
                if task_count:
                    ans += task_count[-1][0]
                    task_count[-1] = (task_count[-1][0], task_count[-1][1] - 1)
                    print(ans, task_count)
    return ans


if __name__ == '__main__':
    # BABABCB
    tasks = 'ABBABBC'
    k = 3
    print(optimize_sequence(tasks, k))
