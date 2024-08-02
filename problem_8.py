# This problem was asked by Palantir.
# The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.


def solve(a, b):    
    # our purpose is convert a/b to something like 1/x + 1/y + 1/z
    # a/b = 1/i + (a/b - 1/i) = 1/i + (a * i - b / (b * i))
    # then apply same logic with ((a * i - b) / (b * i)) until a * i - b == 1

    if(a == 1):
        return f"1/{b}"
    
    result = []
    while(a > 1):
        i = 1
        while(a * i < b):
            i += 1

        result.append(f"1/{i}")

        a = (i * a) - b
        if(a == 1):
            result.append(f"1/{b}")
            break
        b = i * b

    return " + ".join(result)    

if __name__ == '__main__':
    print(solve(4, 13))