import json

def sum_all_numbers(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_all_numbers(item) for item in data)
    elif isinstance(data, dict):
        return sum(sum_all_numbers(value) for value in data.values())
    return 0

def sum_all_numbers_part2(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_all_numbers_part2(item) for item in data)
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(sum_all_numbers_part2(value) for value in data.values())
    return 0

with open("day12.json", "r") as f:
    data = json.load(f)

print("Part 1:", sum_all_numbers(data))
print("Part 2:", sum_all_numbers_part2(data))
