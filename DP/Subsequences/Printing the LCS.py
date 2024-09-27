#Logic: similar to previous, but also have a set in each dp entry. The set is updated according to the logic below.
#The problem is to print every subsequence in lexicographic order.
class Solution:
    def all_longest_common_subsequences(self, s, t):
        m, n = len(s), len(t)
        
        # Initialize the DP table
        dp = [[(0, set()) for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Build the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, extend the LCS by 1
                    lcs_length = dp[i - 1][j - 1][0] + 1
                    lcs_set = {seq + s[i - 1] for seq in dp[i - 1][j - 1][1]} or {s[i - 1]}
                    dp[i][j] = (lcs_length, lcs_set)
                else:
                    # If characters don't match, take the maximum LCS from previous cells
                    if dp[i - 1][j][0] > dp[i][j - 1][0]:
                        dp[i][j] = dp[i - 1][j]
                    elif dp[i - 1][j][0] < dp[i][j - 1][0]:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        combined_set = dp[i - 1][j][1].union(dp[i][j - 1][1])
                        dp[i][j] = (dp[i - 1][j][0], combined_set)
        
        # The result is in dp[m][n], which contains the length and all LCSs
        lcs_length, lcs_set = dp[m][n]
        
        # Sort the set to return a sorted list of the longest common subsequences
        return sorted(list(lcs_set))
