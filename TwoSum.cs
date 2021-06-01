// URL: https://leetcode.com/problems/two-sum/
// O(n) time complexity where n is the length of nums
// O(n) space complexity since the dictionary can contain all nums values 
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Go through nums array and check if target - nums is
        // already in array keys. If so, return the values of those two
        // keys which contain the indices of those numbers
        // dict = <value, index>
        Dictionary<int, int> dict = new Dictionary<int, int>();
        int currNum;
        for (int i = 0; i < nums.Length; i++)
        {
            currNum = nums[i];
            if (dict.ContainsKey(target - currNum))
            {
                return new int[]{i, dict[target - currNum]};
            }
            else
            {
                dict[currNum] = i;
            }
        }
        
        return null;
    }
}
