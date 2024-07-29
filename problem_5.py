# This problem was asked by Microsoft.

# Given a number in the form of a list of digits, return all possible permutations.

# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def solve(digits):
    l = len(digits)
    x = y = 0
    result = []
    while(x < l):
        y = 0
        while(y < l - 1):
            tmp = digits[y + 1]
            digits[y + 1] = digits[y]
            digits[y] = tmp
            result.append(digits.copy())
            y += 1
        x += 1
        
    return result

if __name__ == '__main__':
    print(solve([1,2,3])) # [[2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
    print(solve([1,2,3,4])) # [[2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1], [3, 2, 4, 1], [3, 4, 2, 1], [3, 4, 1, 2], [4, 3, 1, 2], [4, 1, 3, 2], [4, 1, 2, 3], [1, 4, 2, 3], [1, 2, 4, 3], [1, 2, 3, 4]]