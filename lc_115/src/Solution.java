class Solution {
    public int numDistinct(String S, String T) {
        int[][] dp = new int[S.length()+1][T.length()+1];
        for (int i = 0; i < S.length()+1; i++)
            dp[i][0] = 1;
        for (int j = 0; j < T.length(); j++) {
            for (int i = j; i < S.length(); i++) {
                if (S.charAt(i) == T.charAt(j)) {
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1];
                } else {
                    dp[i + 1][j + 1] = dp[i][j + 1];
                }
            }
        }
        return dp[S.length()][T.length()];
    }

    public static void main (String[] args) {
        Solution s = new Solution();
        System.out.print(s.numDistinct("babgbag", "bag"));
    }
}