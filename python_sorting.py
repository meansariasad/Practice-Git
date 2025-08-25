def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order.

    Args:
        numbers (list): List of numbers to sort.

    Returns:
        list: Sorted list of numbers.
    """
    return sorted(numbers)

if __name__ == "__main__":
    # Example usage
    nums = [5, 2, 9, 1, 5, 6]
    print("Original list:", nums)
    sorted_nums = sort_numbers(nums)
    print("Sorted list:", sorted_nums)