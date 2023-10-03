import java.util.HashSet;

public class FindDuplicates {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 2, 5, 6, 4};
        
        // Create a HashSet to store unique elements
        HashSet<Integer> uniqueElements = new HashSet<>();
        
        // Create a HashSet to store duplicate elements
        HashSet<Integer> duplicateElements = new HashSet<>();
        
        for (int num : arr) {
            if (!uniqueElements.add(num)) {
                // If the element is already in uniqueElements, it's a duplicate
                duplicateElements.add(num);
            }
        }
        
        System.out.println("Duplicate elements in the array: " + duplicateElements);
    }
}
