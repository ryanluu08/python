def longestCommonPrefix(strs):
    # Handle edge case where the input list is empty
    if not strs:
        return ""

    # Find the minimum length of strings in the list
    min_len = min(len(s) for s in strs)

    # Initialize the common prefix
    common_prefix = ""

    # Iterate through characters up to the minimum length
    for i in range(min_len):
        # Get the character at the current position in the first string
        char = strs[0][i]

        # Check if the character is the same in all strings
        if all(s[i] == char for s in strs):
            common_prefix += char
        else:
            # If a mismatch is found, stop iterating
            break

    return common_prefix

# Example usage:
strs1 = ["fleower", "fleow", "fleight"]
print(longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))  # Output: ""

