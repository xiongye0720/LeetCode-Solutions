# Approach

For each string, use `alpha`, an array of length 26, to count the occurrences of each letter. Then convert it into a hashable tuple to use as a key in the dictionary `words`. Strings with the same counts are added to the same list. Finally, collect all groups into `res` and return it.

# Correctness

Two strings are anagrams if and only if every letter occurs the same number of times in both strings, meaning their `alpha` tuples are identical. Therefore, strings in the same group must be anagrams, and strings that are anagrams must be placed in the same group.

Each string is added exactly once, and all groups are collected at the end, so the result is complete with no omissions.

# Complexity

Let the number of strings be `n`, the total number of characters be `L`, and the number of groups be `g`.

- **Time complexity:** `O(L + 26n)` on average, which is `O(L+n)`. Counting characters takes `O(L)`, while initializing the count array, converting it to a tuple, and computing its hash take `O(26)` for each string.
- **Space complexity:** `O(n+26g)`, which is `O(n)`. The dictionary stores the count tuple for each group and a total of `n` string references; the string contents are not copied.