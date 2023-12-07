def count_occurrences(batch, pattern):
    if not isinstance(batch, list) or not isinstance(pattern, str):
        raise ValueError("Invalid input parameters for count_occurrences")

    return sum(1 for word in batch if word == pattern)
