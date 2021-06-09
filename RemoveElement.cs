// URL: https://leetcode.com/problems/remove-element/
public class Solution {
    public int RemoveElement(int[] nums, int val) {
        // Have a slow runner (i) and a fast runner (j)
        // If there's a num at an index not equal
        // to val, then increment i, which will represent
        // the length of good non-val numbers and the last good index
        // that can be swapped with the element equal to val
        // O(n) time complexity
        // O(1) space complexity since elements are sorted in place
        int i = 0;
        for (int j = 0; j < nums.Length; j++)
        {
            if (nums[j] != val)
            {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}
