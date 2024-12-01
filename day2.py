# Move All Zeroes to End
# Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

class Solution:
	def pushZerosToEnd(self,arr):
	    
    	last_non_zero_index = 0

        # Traverse the array
        for i in range(len(arr)):
        # If the current element is not zero, we need to move it to the last_non_zero_index
            if arr[i] != 0:
                
                arr[last_non_zero_index] = arr[i]
                last_non_zero_index += 1

    # After all non-zero elements have been moved, fill the rest of the array with zeros
        for i in range(last_non_zero_index, len(arr)):
            arr[i] = 0

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
