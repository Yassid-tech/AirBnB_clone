# This is a simple Python script that adheres to PEP 8 style guide

def calculate_average(numbers):
    """
    This function takes a list of numbers and returns their average.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
