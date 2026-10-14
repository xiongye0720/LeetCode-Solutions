# Approach

Use “the maximum amount when the current house must be robbed” as the state.

- `ops` stores the maximum amounts with each of the two most recent houses as the last house robbed.
- When processing house `i`, `ops.popleft()` retrieves the maximum amount with house `i - 2` as the last house robbed.
- After the update, `maxVal` represents the maximum amount when the last house robbed is at or before `i - 2`. Therefore, `maxVal + nums[i]` is the maximum amount when house `i` must be robbed. Add this value to the queue.

If there are only one or two houses, directly return the corresponding maximum amount.

# Correctness

When robbing house `i`, the previous house robbed must be between `0` and `i - 2`. `maxVal` maintains exactly the maximum among the states for these positions. Therefore, each new state added to the queue satisfies the restriction that adjacent houses cannot both be robbed and achieves the maximum amount for that state.

The amount in each house is nonnegative. If a plan's last house robbed is before the final two houses, the last house can also be robbed without reducing the total amount. Therefore, there is always an optimal plan whose last house robbed is one of the final two houses, so returning `max(ops)` gives the answer.

# Complexity

Let the number of houses be `n`.

- **Time Complexity:** `O(n)`. Iterate over the houses and perform a constant number of state updates each time.
- **Auxiliary Space Complexity:** `O(1)`. The queue always stores at most two states, and the remaining variables use constant space.