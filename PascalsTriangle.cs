// URL: https://leetcode.com/problems/pascals-triangle/
// Strategy here is to iterate over each row, adding 1s to the sides
// of the rows where necessary and adding the curren above two items
// when needed.
// O(n) time complexity to add element for every n element
// O(n) space complexity where n is the number of elements in all rows
public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        IList<IList<int>> result = new List<IList<int>>();
            
        if (numRows < 1) {
            return result;
        }
        List<int> previousRow = new List<int>();
        previousRow.Add(1);
        
        result.Add(previousRow);
        
        for (int i = 0; i < numRows - 1; i++) {
            previousRow = new List<int>();
            previousRow.Add(1);
            for (int j = 0; j < result[i].Count; j++) {
                if (j == result[i].Count - 1){
                    previousRow.Add(result[i][j]);
                } else {
                    previousRow.Add(result[i][j] + result[i][j + 1]);
                }
            }
            result.Add(previousRow);
        }
        
        return result;
    }
}
