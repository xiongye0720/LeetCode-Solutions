# Approach

The window uses the half-open interval `[left, right)`:

- `tDict` records the required count of each target character.
- `sDict` records the count of each target character in the window.
- `diff` records the number of distinct characters whose counts meet the requirements. Therefore, `diff == len(tDict)` means the window fully covers `t`.

For each `left`, the code expands the window to the right until it fully covers the target. It then records a shorter answer, removes the leftmost character, and advances `left`. If the requirements are still met after removal, the next iteration can continue shrinking the window directly.

When a character's count increases to the required count, increase `diff` by one. When it decreases to one below the required count, decrease `diff` by one. Repeated characters beyond the required count do not change the coverage state.

# Correctness

`diff` is updated only when a character's count crosses its coverage threshold, so it always accurately represents the number of distinct characters that meet the requirements.

For the current left endpoint, the right endpoint stops at the earliest position that covers the target:

- If the window does not yet cover the target, add characters one at a time and stop as soon as it does.
- If the window already covers the target, no expansion is needed. Earlier right endpoints could not cover the target, and removing the leftmost character cannot make them valid.

Therefore, the code checks the shortest valid window for each left endpoint and uses `minLen` to keep the shortest one among them.

If the right endpoint reaches the end of the string without covering the target, moving the left endpoint further will only remove characters and cannot restore coverage, so the loop can end immediately. If no valid window is found, return an empty string; otherwise, return the recorded substring.

# Complexity

Let `m = len(s)`, `n = len(t)`, and `k` be the number of distinct characters in `t`:

- **Time complexity: O(m+n)**. Building the target counts takes O(n), and each pointer advances at most O(m) times.
- **Auxiliary space complexity: O(k)**. Both dictionaries store only target characters. The returned substring requires an additional O(L) space, where `L` is the answer length.