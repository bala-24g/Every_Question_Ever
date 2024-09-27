#Longest palindromic subsequence

# LOGIC:1.Longest palindromic subsequence: this is apparently same as finding the longest common subsequence between 2 strings, but one string just reverse of the other. How you’ve to do it is that u initialise the dp array with 0s of length len(s)+1 squared; where dp[i][j] represents the longest palindromic subsequence with the substrings s[0:i], reverse[0:j]. You check if s[i-1]==r[j-1] , if it is dp[i][j]=dp[i-1][j-1]+1 else it is max(dp[i-1][j],dp[i][j-1]).
def longestPalinSubseq(S):
    R = S[::-1]

    # dp[i][j] will store the length of the longest
    # palindromic subsequence for the substring
    # starting at index i and ending at index j
    dp = [[0] * (len(R) + 1) for _ in range(len(S) + 1)]

    # Filling up DP table based on conditions discussed
    # in the above approach
    for i in range(1, len(S) + 1):
        for j in range(1, len(R) + 1):
            if S[i - 1] == R[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # At the end, DP table will contain the LPS
    # So just return the length of LPS
    return dp[len(S)][len(R)]


# Driver code
s = "GEEKSFORGEEKS"
print("The length of the LPS is", longestPalinSubseq(s))

# This code is contributed by shivamgupta310570
