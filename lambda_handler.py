import json

def validate_input(event):
    if not event or not isinstance(event, dict) or 'text' not in event or 'pattern' not in event or 'batch_size' not in event:
        raise ValueError("Invalid input event structure")

    text = event['text']
    pattern = event['pattern']
    batch_size = event['batch_size']

    if not isinstance(text, str) or not isinstance(pattern, str) or not isinstance(batch_size, int) or batch_size <= 0:
        raise ValueError("Invalid input parameters")

    return text, pattern, batch_size

def lambda_handler(event, context):
    try:
        # Validate input
        text, pattern, batch_size = validate_input(event)

        # Divide into batches
        batches = divide_into_batches(text, batch_size)

        # Count occurrences in each batch
        occurrences_list = [count_occurrences(batch, pattern) for batch in batches]

        # Sum up overall occurrences
        total_occurrences = sum_occurrences(occurrences_list)

        return {
            'total_occurrences': total_occurrences,
            'batches': batches  # Include batches for demonstration purposes
        }

    except ValueError as ve:
        # Handle validation errors
        return {
            'error': str(ve)
        }

    except Exception as e:
        # Handle other exceptions and log errors
        return {
            'error': str(e)
        }
