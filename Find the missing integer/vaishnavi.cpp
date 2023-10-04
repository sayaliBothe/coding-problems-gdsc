#include <iostream>
#include <vector>

int findMissingInteger(std::vector<int>& nums) {
    int missing = 0;
    
    for (int i = 0; i < nums.size(); ++i) {
        missing ^= nums[i];
    }
    
    for (int i = 1; i <= nums.size() + 1; ++i) {
        missing ^= i;
    }
    
    return missing;
}

int main() {
    std::vector<int> nums = {1, 2, 4, 6, 3, 7, 8};
    int missing = findMissingInteger(nums);
    
    std::cout << "The missing integer is: " << missing << std::endl;
    
    return 0;
}
