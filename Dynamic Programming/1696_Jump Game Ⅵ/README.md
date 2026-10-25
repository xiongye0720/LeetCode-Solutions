# Approach

`maxScore[i]` represents the maximum score upon reaching position `i`. It can be reached from any of the previous `k` positions:

`maxScore[i] = score[i] + max(maxScore[j])`

where `j` satisfies `max(0,i-k) ≤ j < i`.

`ops` stores the indices of candidate positions in increasing order, with their corresponding `maxScore` values strictly decreasing. Therefore, the front of the deque always provides the maximum score currently available.

After computing the current state, remove indices from the back whose scores are no greater than `maxScore[i]`, then add `i`. Finally, remove the front index if it has expired for the next iteration.

# Correctness

For any position removed from the back, the current position `i` has a score at least as high, a larger index, and a later expiration. Therefore, whenever the old position can be used in a future transition, `i` can also be used and provides a score at least as high. Removing the old position does not affect the optimal result.

The expiration check occurs after the calculation because position `i-k` is still valid for the current state but becomes invalid in the next iteration. The window advances by only one position per iteration, so at most one additional index expires. Thus, a single `popleft()` is sufficient.

Therefore, before each calculation, the deque contains only valid candidates, and the score at the front is the maximum. The transition correctly computes `maxScore[i]`. Finally, returning `maxScore[-1]` gives the answer.

# Complexity

Let the array length be `n`.

- **Time Complexity:** `O(n)`. Each index enters the deque once and is removed at most once, either from the front or the back.
- **Auxiliary Space Complexity:** `O(n)`. `maxScore` stores `n` states, and the deque temporarily stores at most `min(n,k+1)` indices. `score` only references the original array.