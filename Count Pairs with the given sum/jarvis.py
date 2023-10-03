def count_pairs_with_sum(arr, target_sum):
    # Create a dictionary to store the frequency of each number in the array
    num_freq = {}
    count = 0

    # Iterate through the array
    for num in arr:
        # Calculate the complement required to reach the target sum
        complement = target_sum - num

        # Check if the complement exists in the dictionary
        if complement in num_freq:
            # Increment the count with the frequency of the complement
            count += num_freq[complement]

        # Update the frequency of the current number
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1

    return count

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
target_sum = 7
result = count_pairs_with_sum(arr, target_sum)
print("Number of pairs with sum", target_sum, ":", result)
