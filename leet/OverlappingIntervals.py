class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def find_overlapping(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x: x.start)
    currend, count = intervals[0].end, 0

    for i in intervals[1:]:
        if i.start < currend:
            count += 1
            currend = min(currend, i.end)
        else :
            currend = i.end

    return count




if __name__ == '__main__':
    intervals = [Interval(1,2), Interval(2,3), Interval(3,4), Interval(1,3)]
    print(find_overlapping(intervals))