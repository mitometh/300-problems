# This problem was asked by Apple.
# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

def solve(n) -> int:
    # Fibonacci sequence: 0, 1, 2, 3, 5, 8, 13
    # fib(n) = fib(n - 1) +  fib(n - 2)

    if(n <= 2):
        return n
        
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, curr + prev

    return curr

if __name__ == '__main__':
    print(solve(7))