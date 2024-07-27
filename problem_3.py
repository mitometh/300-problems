# This problem was asked by Facebook.
# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

def solve(trap):
    if not trap:
        return 0

    # I use 2-pointers technique and update max height which related to current trap inde
    # We move left and right pointer until they meet each other
    # When moving the pointer, we calculate trapped water by using (max height - current height) of the side. In same time, we update max height (if need)

    left, right = 0, len(trap) - 1
    left_max, right_max = trap[left], trap[right]
    water_trapped = 0

    while left < right:
        if trap[left] < trap[right]:
            left += 1
            left_max = max(left_max, trap[left])
            water_trapped += max(0, left_max - trap[left])
        else:
            right -= 1
            right_max = max(right_max, trap[right])
            water_trapped += max(0, right_max - trap[right])

    return water_trapped

if __name__ == '__main__':
    print(solve([2, 1, 2]))  # Output should be 1
    print(solve([3, 0, 1, 3, 0, 5]))  # Output should be 8