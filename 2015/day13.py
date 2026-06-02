from functools import cache

def dp_val(start, node_set, happiness):
    # To memoize, we need a hashable inner function since sets and dicts are not hashable.
    # We use frozenset for the set, and reference happiness from the outer scope.
    @cache
    def helper(curr, remaining):
        if not remaining:
            # Base case: no more nodes to visit, return to start to complete the cycle
            return happiness[(curr, start)] + happiness[(start, curr)]
        
        max_val = -float('inf')
        for next_node in remaining:
            new_remaining = remaining - frozenset([next_node])
            val = (helper(next_node, new_remaining) 
                   + happiness[(curr, next_node)] 
                   + happiness[(next_node, curr)])
            max_val = max(max_val, val)
        return max_val

    # Convert the input set to an immutable frozenset
    initial_set = frozenset(node_set) - {start}
    return helper(start, initial_set)

happiness = {
    ("Alice", "Bob"): 54,
    ("Alice", "Carol"): -81,
    ("Alice", "David"): -42,
    ("Alice", "Eric"): 89,
    ("Alice", "Frank"): -89,
    ("Alice", "George"): 97,
    ("Alice", "Mallory"): -94,
    ("Bob", "Alice"): 3,
    ("Bob", "Carol"): -70,
    ("Bob", "David"): -31,
    ("Bob", "Eric"): 72,
    ("Bob", "Frank"): -25,
    ("Bob", "George"): -95,
    ("Bob", "Mallory"): 11,
    ("Carol", "Alice"): -83,
    ("Carol", "Bob"): 8,
    ("Carol", "David"): 35,
    ("Carol", "Eric"): 10,
    ("Carol", "Frank"): 61,
    ("Carol", "George"): 10,
    ("Carol", "Mallory"): 29,
    ("David", "Alice"): 67,
    ("David", "Bob"): 25,
    ("David", "Carol"): 48,
    ("David", "Eric"): -65,
    ("David", "Frank"): 8,
    ("David", "George"): 84,
    ("David", "Mallory"): 9,
    ("Eric", "Alice"): -51,
    ("Eric", "Bob"): -39,
    ("Eric", "Carol"): 84,
    ("Eric", "David"): -98,
    ("Eric", "Frank"): -20,
    ("Eric", "George"): -6,
    ("Eric", "Mallory"): 60,
    ("Frank", "Alice"): 51,
    ("Frank", "Bob"): 79,
    ("Frank", "Carol"): 88,
    ("Frank", "David"): 33,
    ("Frank", "Eric"): 43,
    ("Frank", "George"): 77,
    ("Frank", "Mallory"): -3,
    ("George", "Alice"): -14,
    ("George", "Bob"): -12,
    ("George", "Carol"): -52,
    ("George", "David"): 14,
    ("George", "Eric"): -62,
    ("George", "Frank"): -18,
    ("George", "Mallory"): -17,
    ("Mallory", "Alice"): -36,
    ("Mallory", "Bob"): 76,
    ("Mallory", "Carol"): -34,
    ("Mallory", "David"): 37,
    ("Mallory", "Eric"): 40,
    ("Mallory", "Frank"): 18,
    ("George", "Mallory"): -17,  # Note: George sitting next to Mallory was listed as George would lose 17 sitting next to Mallory
    ("Mallory", "George"): 7,
    ("Alice", "Me"): 0,
    ("Me", "Alice"): 0,
    ("Bob", "Me"): 0,
    ("Me", "Bob"): 0,
    ("Carol", "Me"): 0,
    ("Me", "Carol"): 0,
    ("David", "Me"): 0,
    ("Me", "David"): 0,
    ("Eric", "Me"): 0,
    ("Me", "Eric"): 0,
    ("Frank", "Me"): 0,
    ("Me", "Frank"): 0,
    ("George", "Me"): 0,
    ("Me", "George"): 0,
    ("Mallory", "Me"): 0,
    ("Me", "Mallory"): 0,
}

# Extract unique people/nodes
nodes = set(p[0] for p in happiness.keys())

if __name__ == "__main__":
    start_node = next(iter(nodes))
    result = dp_val(start_node, nodes, happiness)
    print(f"Optimal happiness: {result}")
