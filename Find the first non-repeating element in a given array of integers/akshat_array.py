from collections import Counter

def first_non_repeating_element(arr):
    # Count the occurrences of each element in the array
    element_count = Counter(arr)

    # Iterate through the array and find the first non-repeating element
    for element in arr:
        if element_count[element] == 1:
            return element

    return None  # Return None if no non-repeating element is found

# Example usage
arr = [9, 3, 2, 6, 6, 1, 9, 2, 4, 3]
first_non_repeating = first_non_repeating_element(arr)
print("First non-repeating element:", first_non_repeating)  # Output: 1
