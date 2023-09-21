def quicksort(numbers):
    """
    Sorts an array of numbers in ascending order using the quicksort algorithm.

    Args:
        numbers (list): The array of numbers to sort.

    Returns:
        list: The sorted array of numbers.
    """
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[0]
    left = []
    right = []
    
    for number in numbers[1:]:
        if number < pivot:
            left.append(number)
        else:
            right.append(number)
    
    return quicksort(left) + [pivot] + quicksort(right)

def sort_array(numbers):
    """
    Sorts an array of numbers in ascending order.

    Args:
        numbers (list): The array of numbers to sort.

    Returns:
        list: The sorted array of numbers.
    """
    return quicksort(numbers)
