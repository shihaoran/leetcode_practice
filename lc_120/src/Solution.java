import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        int[][] dp = new int[triangle.size()][triangle.get(triangle.size()-1).size()];
        dp[0][0] = triangle.get(0).get(0);
        for (int i = 1; i < triangle.size(); i++) {
            for (int j = 0; j <= i; j++) {
                int min = Integer.MAX_VALUE;
                if (j-1>=0) {
                    min = dp[i-1][j-1];
                }
                if (j<i && dp[i-1][j] < min) {
                    min = dp[i-1][j];
                }
                dp[i][j] = triangle.get(i).get(j) + min;
            }
        }
        int minPath = Integer.MAX_VALUE;
        for (int i = 0; i < triangle.get(triangle.size()-1).size(); i++) {
            if (dp[triangle.size()-1][i] < minPath) {
                minPath = dp[triangle.size()-1][i];
            }
        }
        return minPath;
    }

    public static void main (String[] args) {
        Solution s = new Solution();
        ArrayList<Integer> w1 = new ArrayList<Integer>();
        w1.add(2);
        ArrayList<Integer> w2 = new ArrayList<Integer>();
        w2.add(3);
        w2.add(4);
        ArrayList<Integer> w3 = new ArrayList<Integer>();
        w3.add(5);
        w3.add(6);
        w3.add(7);
        ArrayList<ArrayList<Integer>> a = new ArrayList<ArrayList<Integer>>();
        a.add(w1);
        a.add(w2);
        a.add(w3);

        System.out.print(s.minimumTotal(a));
    }
}