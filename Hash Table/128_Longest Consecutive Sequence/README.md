# Approach

First, convert `nums` to a set to remove duplicates and support fast lookups.

When iterating over the set, if `item` has not been visited, expand from it one integer at a time to the right and left, adding all consecutive integers found to `visit`.

After expansion, `left` and `right` are the first missing integers on either side of the sequence, so the sequence length is:

`right - left - 1`

Use `maxLen` to track the maximum length, and skip elements that have already been visited.

# Correctness

Starting from any unvisited element, expanding in both directions finds the entire consecutive sequence containing it: no integers are missing within the sequence, and neither boundary exists in the set.

After expansion, the entire sequence is marked as visited, so skipping its elements later does not miss any new sequences. Therefore, each complete consecutive sequence is processed exactly once, and the maximum of their lengths is the answer. If the set is empty, no expansion occurs, and the initial value `0` is returned.

# Complexity

Let the length of the original array be `n`:

- Time complexity: `O(n)` on average. Each consecutive sequence is expanded only once. Its starting element is processed once by each of the left and right loops, while every other element is processed once; the total number of boundary checks is also `O(n)`. Set lookups and insertions take `O(1)` on average.
- Space complexity: `O(n)`, for the set of unique values and `visit`.