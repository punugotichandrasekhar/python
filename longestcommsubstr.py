def longest_common_substring(s1, s2):
    # Get lengths of both strings
    m = len(s1)
    n = len(s2)
    
    # Create a 2D array to store lengths of longest common suffixes
    # Initialize all cells to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variable to store the length of the longest common substring
    longest_length = 0

    # Variable to store the ending index of the longest common substring in s1
    end_index = 0

    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    # The longest common substring is from s1[end_index - longest_length:end_index]
    return s1[end_index - longest_length:end_index]

# Example usage
s1 = "abcdef"
s2 = "zabcdf"

result = longest_common_substring(s1, s2)
print(f"Longest Common Substring: {result}")
