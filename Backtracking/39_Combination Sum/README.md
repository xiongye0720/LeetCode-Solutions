# Approach

First, sort `candidates` in ascending order, then use DFS to determine how many times to use each candidate.

- `lvl` indicates which candidate is currently being processed, and `amt` is the usage count chosen for this call.
- `proc[i]` stores the usage count of `candidates[i]`, and `rem[0]` stores the remaining target value.
- Each call first records `amt` and subtracts `amt * candidates[lvl-1]`. It then enumerates the usage count of the next candidate, ranging from `0` to `rem[0] // candidates[lvl]`.
- End the current branch when all candidates have been processed or the remaining value is smaller than the next candidate. If the remaining value is zero, expand the counts in `proc` into a combination and save it.
- Before returning, pop the count recorded in this call and restore the remaining value so that other branches start from the same state.

# Correctness

The candidates in the problem are distinct positive integers. Each enumerated count keeps the remaining value non-negative, so whenever a result is saved, the sum of the combination is exactly `target`.

After sorting, if the remaining value is smaller than the next candidate, none of the larger candidates can be used either. If the remaining value is zero, the combination is complete; otherwise, the branch has no solution. Therefore, ending the branch early does not miss any results.

Each valid combination corresponds to a unique set of usage counts. The code enumerates all feasible counts in order, so no combination is missed. Processing candidates in a fixed order also ensures that the same combination is not generated more than once due to different element orders.

# Complexity

Let the number of candidates be `m`, the actual number of DFS calls be `V`, the number of results be `K`, and the total number of elements across all results be `S`.

- **Time complexity:** `O(m log m + V + Km + S)`. These terms correspond to sorting, searching, scanning the usage counts, and filling the results with elements, respectively. The search size can grow exponentially in the worst case.
- **Auxiliary space complexity:** `O(m)`, for the recursion stack, `proc`, and the space required for sorting.
- **Space complexity including the returned results:** `O(m + S)`.