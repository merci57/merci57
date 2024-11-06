def string_lengths(strings):
    string_length = {s: len(s) for s in strings}
    return string_length

# Example usage
strings = ["apple", "banana", "orange"]
result = string_lengths(strings)
print(result)