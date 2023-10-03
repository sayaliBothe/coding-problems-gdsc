def subarray_with_given_sum(arr, target_sum):
    if not arr:
        return None

    current_sum = arr[0]
    start = 0

    for end in range(1, len(arr)):
        # Remove elements from the start until the sum is less than or equal to the target sum
        while current_sum > target_sum and start < end:
            current_sum -= arr[start]
            start += 1

        # If the sum matches the target sum, return the subarray
        if current_sum == target_sum:
            return arr[start:end]

        # Add the current element to the sum
        current_sum += arr[end]

    # Check for the last subarray
    while current_sum > target_sum and start < len(arr):
        current_sum -= arr[start]
        start += 1

    if current_sum == target_sum:
        return arr[start:]

    return None

# Example usage
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
result_subarray = subarray_with_given_sum(arr, target_sum)
print("Subarray with the given sum:", result_subarray)  # Output: [20, 3, 10]
