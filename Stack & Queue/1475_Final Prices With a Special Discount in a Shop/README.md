# Approach

`nextIdx[i]` represents the first position to the right whose price is no greater than `price[i]`, or `-1` if no such position exists.

Process from right to left, setting `temPtr` to the adjacent position each time:

- If `price[temPtr] ≤ price[right]`, the discount position has been found.
- Otherwise, continue searching along `nextIdx[temPtr]`. If it is `-1`, no valid position exists.

Finally, use `nextIdx` to calculate the final price of each item and store it in `resList`.

# Correctness

When processing `right`, all `nextIdx` values to its right have already been correctly computed.

When `price[right] < price[temPtr]`, `temPtr` does not satisfy the condition. Since `nextIdx[temPtr]` is the first position to its right whose price is no greater than its own, all prices between these two positions are greater than `price[temPtr]` and therefore greater than `price[right]`. Thus, these positions can be skipped directly.

If `nextIdx[temPtr]` is `-1`, all prices to its right are greater than its own, so none can provide a discount either. Each jump only excludes positions that do not satisfy the condition, so the position eventually found must be the first valid position to the right.

# Complexity

Let the number of items be `n`.

- **Time Complexity:** `O(n)`. The candidate positions in the processed range are linked through `nextIdx`. Each time a candidate is skipped, the link from the new position bypasses it, removing it from the candidate chain used in subsequent searches. Each position is removed at most once, so all jumps take `O(n)` in total. Constructing the final result also takes `O(n)`.
- **Auxiliary Space Complexity:** `O(n)`. `nextIdx` stores the discount index for each position. The returned result `resList` uses an additional `O(n)` space, while `price` only references the original list.