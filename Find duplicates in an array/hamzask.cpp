#include <iostream>
#include <unordered_set>
#include <vector>

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 2, 5, 6, 3};

    std::unordered_set<int> seen;
    std::cout << "Duplicate elements in the array are: ";

    for (int num : arr) {
        if (seen.find(num) == seen.end()) {
            seen.insert(num);
        } else {
            std::cout << num << " ";
        }
    }

    std::cout << std::endl;

    return 0;
}
