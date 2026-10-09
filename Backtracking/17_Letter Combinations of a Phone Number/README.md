# Approach

The code uses DFS to choose a letter for each digit.

- The outer loop iterates over the letters corresponding to the first digit and starts the recursion.
- `currChar` stores the prefix generated so far, and `lvl` is the index of the last processed digit.
- Each level iterates over the letters corresponding to `digits[lvl+1]` and extends the prefix using `currChar + item`.
- When `lvl == maxLvl`, all digits have been processed, so the complete string is added to `ans`.

String concatenation creates a new string without modifying the original prefix, so there is no need to explicitly restore state between recursive branches.

# Correctness

Each level chooses exactly one corresponding letter for one digit, so every saved string has the required length and uses letters from the correct digits.

The code explores all letter choices for every digit, so no combination is missed. Different choice paths select different letters at at least one position, so no duplicate results are generated.

# Complexity

Let the number of digits be `n`, with `7` and `9` appearing a total of `t` times. The number of results is:

`K = 3^(n-t) · 4^t`

- **Time complexity:** `O(nK)`. Each concatenation copies the prefix, and the total concatenation cost across all levels is `O(nK)`.
- **Auxiliary space complexity:** `O(n²)`. The recursion depth is `n`, and the recursive levels simultaneously retain prefix strings of increasing lengths, with a total length of `O(n²)`.
- **Space complexity including the returned results:** `O(nK)`, for storing `K` strings of length `n`.