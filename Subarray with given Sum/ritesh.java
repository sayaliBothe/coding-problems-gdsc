public class SubarrayWithGivenSum {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int targetSum = 11;

        findSubarrayWithSum(arr, targetSum);
    }

    public static void findSubarrayWithSum(int[] arr, int targetSum) {
        int currentSum = 0;
        int start = 0;

        for (int end = 0; end < arr.length; end++) {
            currentSum += arr[end];

            while (currentSum > targetSum && start < end) {
                currentSum -= arr[start];
                start++;
            }

            if (currentSum == targetSum) {
                System.out.println("Subarray found from index " + start + " to " + end);
                return;
            }
        }

        System.out.println("No subarray found with the given sum.");
    }
}
