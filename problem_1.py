# This problem was asked by Snapchat.
# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
# The input list is not necessarily ordered in any way.
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

def resolve(intervals):
    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last = merged_intervals[-1]

        if(current[0] < last[1]):
            merged_intervals[-1] = (last[0], max(last[1], current[1]))
        else:
            merged_intervals.append(current)

    return merged_intervals


if __name__ == '__main__':
    result = resolve([(1, 3), (4, 10), (20, 25)])
    print(result)
