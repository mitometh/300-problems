# This problem was asked by Jane Street.

# The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.
# Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.


from collections import deque

def add_relationship(graph, var1, var2, factor): #var1 = var2/factor
    if var1 not in graph:
        graph[var1] = {}
    if var2 not in graph:
        graph[var2] = {}
    graph[var1][var2] = factor
    graph[var2][var1] = 1 / factor


def find_conversion(graph, start, end):
    if start not in graph or end not in graph:
        return None

    queue = deque([(start, 1)])
    visited = set()

    while queue:
        current, factor = queue.popleft()

        if current == end:
            return factor

        visited.add(current)

        for neighbor, conversion_factor in graph[current].items():
            if neighbor not in visited:
                queue.append((neighbor, factor * conversion_factor))

    return None  # If no path is found

def solve(graph, start, end):
    return find_conversion(graph, start, end)


if __name__ == '__main__':
    graph = {}

    # Add relationships: a = 1/x of b, b = 1/y of c
    add_relationship(graph, 'inch', 'foot', 12)
    add_relationship(graph, 'foot', 'yard', 3)
    add_relationship(graph, 'yard', 'chain', 22)
    add_relationship(graph, 'metre', 'yard', 0.9144)
    add_relationship(graph, 'centimetre', 'metre', 100)

    print(solve(graph, 'inch', 'centimetre'))
