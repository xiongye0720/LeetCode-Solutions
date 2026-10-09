# Approach

`col[0]` stores the current candidate, and `col[1]` stores its occurrence count that has not yet been canceled out.

When traversing the array:
- If there is no candidate, set the current element as the candidate and set the count to `1`.
- If the current element matches the candidate, increase the count by one.
- If the current element differs from the candidate, decrease the count by one. If the count reaches zero, clear the candidate.

This process is equivalent to repeatedly removing two different elements. The majority element appears more than half the length of the array, and each cancellation removes at most one occurrence of it, so it cannot be completely canceled out. After the traversal, the remaining candidate must be the majority element.

The problem guarantees that a majority element exists, so `col[0]` can be returned directly without further verification.

# Complexity

- Time complexity: `O(n)`, since the array is traversed once.
- Space complexity: `O(1)`, since only the candidate and its count are maintained.