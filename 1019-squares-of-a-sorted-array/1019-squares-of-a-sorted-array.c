#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int *returnArray = malloc(numsSize * sizeof(int));   
    
    int first = 0;
    int last = numsSize-1;
    
    for(int i = last; i >= 0; i--){
        if(abs(nums[first]) > abs(nums[last])){
            returnArray[i] = nums[first] * nums[first];
            first++;
        }
        else{
            returnArray[i] = nums[last] * nums[last];
            last--;
        }
        
    }
    *returnSize = numsSize;
    return returnArray;
}