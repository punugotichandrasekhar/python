def permute(s, path=""):
    if len(s) == 0:
        print(path)
    else:
        for i in range(len(s)):
            # Choose the current element and generate the remaining permutations
            permute(s[:i] + s[i+1:], path + s[i])

# The original string
s = "123"

# Call the permute function
permute(s)
