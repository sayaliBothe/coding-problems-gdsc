def find_duplicates(arr):
    # Create an empty set to store unique elements
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen:
            # If the element is already in the set, it's a duplicate
            duplicates.append(num)
        else:
            # Otherwise, add it to the set
            seen.add(num)

    return duplicates

# Example usage:
arr = [1, 2, 3, 4, 2, 5, 6, 4]
duplicate_elements = find_duplicates(arr)
print("Duplicate elements in the array:", duplicate_elements)
