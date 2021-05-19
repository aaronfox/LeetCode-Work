// URL: https://leetcode.com/problems/pascals-triangle-ii/
// This keeps track of previous row and current row and builds on that.
// This solution could be optimized by not using two different rows
// O(k) runtime complexity to iterate over every possible row element
// O(n) space complexity for storing 2 rows in lists of max length rowIndex (n).
public class Solution {
    public IList<int> GetRow(int rowIndex) {

        List<int> previousRow = new List<int>();

        previousRow.Add(1);
        if (rowIndex < 1) {
            return previousRow;
        }
        
        List<int> currentRow;
        
        for (int i = 0; i < rowIndex; i++) {
            
            currentRow = new List<int>();
            currentRow.Add(1);
            for (int j = 0; j < previousRow.Count - 1; j++) {
                currentRow.Add(previousRow[j] + previousRow[j + 1]);
            }
            currentRow.Add(1);
            
            
            previousRow = currentRow;
        }
        
        return previousRow;
    }
}
