def edit_distance(s1, s2):
    # Input validation
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both inputs must be strings.")

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # If s1 is empty, all characters of s2 need to be inserted
            elif j == 0:
                dp[i][j] = i  # If s2 is empty, all characters of s1 need to be deleted
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                   dp[i][j - 1],    # Insertion
                                   dp[i - 1][j - 1]) # Substitution

    return dp[m][n]

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("horse", "ros"),  # Output: 3
        ("intention", "execution"),  # Output: 5
        ("", ""),  # Output: 0
        ("a", "b"),  # Output: 1
        ("abc", "yabd"),  # Output: 2
        ("kitten", "sitting"),  # Output: 3
        ("flaw", "lawn")  # Output: 2
    ]
    
    for s1, s2 in test_cases:
        distance = edit_distance(s1, s2)
        print(f"The edit distance between '{s1}' and '{s2}' is: {distance}")
