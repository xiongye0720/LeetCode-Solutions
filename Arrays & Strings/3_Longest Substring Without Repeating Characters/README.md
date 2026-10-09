# Approach

Maintain a window `[left, right)`, with `charSet` storing the characters in the window.

Keep expanding the right end until `s[right]` is already in the set or the end of the string is reached, then update `maxLen` with `right-left`.

After encountering a duplicate character, remove one character from the left end in each iteration. If the duplicate remains, the right end stays in place in the next iteration; it continues expanding only after the original occurrence of the duplicate character is removed. For an empty string, return 0 directly.

# Correctness

Only characters that are not in `charSet` are added to the window, so the window never contains duplicate characters, and the set accurately represents the window's contents.

For each left endpoint, the right end expands until it cannot go any further. At this point, the window is the longest substring without duplicate characters starting at that left endpoint. Moving the left end to the right does not introduce duplicates into the existing window, so the right end does not need to move backward. Updating the maximum length at each step gives the answer.

When `right` reaches the end, the answer has already been updated for the current window. Moving the left end further to the right would only shorten the window, so the process can stop immediately.

# Complexity

Let the string length be `n` and the number of distinct characters be `u`.

- **Time complexity:** average `O(n)`. Set operations take `O(1)` time on average. Both pointers only move to the right, and each character is added to and removed from the set at most once.
- **Space complexity:** `O(u)`. The set stores only the distinct characters in the current window.