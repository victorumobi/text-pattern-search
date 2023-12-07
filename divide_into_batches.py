import re

def divide_into_batches(text, batch_size):
    if not isinstance(text, str) or not isinstance(batch_size, int) or batch_size <= 0:
        raise ValueError("Invalid input parameters for divide_into_batches")

    words = re.findall(r'\b\w+\b', text)
    batches = [words[i:i + batch_size] for i in range(0, len(words), batch_size)]
    return batches

