# This problem was asked by PagerDuty.

# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.


def solve(n):
    path = [n]
    step = 0
    while(n > 1):
        max_i = 1
        for i in range(2, int(n ** 0.5) + 1):
            if(n % i  == 0):
                max_i = i

        if(max_i != 1):
            n = max(max_i, n//max_i)
        else:
            n -= 1

        path.append(n)

        step += 1

    return step, path
    


if __name__ == '__main__':
    print(solve(120))