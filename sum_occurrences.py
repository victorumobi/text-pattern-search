def sum_occurrences(occurrences_list):
    if not isinstance(occurrences_list, list):
        raise ValueError("Invalid input parameters for sum_occurrences")

    return sum(occurrences_list)
