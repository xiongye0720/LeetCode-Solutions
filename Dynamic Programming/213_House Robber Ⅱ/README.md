# Approach

Let the number of houses be `n`. When `n ≤ 3`, at most one house can be robbed, so directly return the maximum amount.

For the remaining cases, enumerate the house that must be robbed, exclude its two adjacent houses, and pass the remaining problem to `maxValue`:

| `i` | House that must be robbed | Remaining available range (inclusive) |
| --- | --- | --- |
| `0` | `n - 1` | `1` to `n - 3` |
| `1` | `0` | `2` to `n - 2` |
| `2` | `1` | `3` to `n - 1` |

Store the amounts for the three plans in `dp`, then take the maximum.

`maxValue` finds the maximum amount that can be robbed within a linear range. The queue `ops` stores the maximum amounts with each of the two most recent houses as the last house robbed. Each time, remove the earlier state and update `temVal` so that it represents the maximum amount when the last house robbed is at least two positions before the current house. Then add the state `temVal + nums[start+i]`, in which the current house must be robbed.

# Correctness

In `maxValue`, `temVal` covers all previous states compatible with robbing the current house, so each generated state is valid and optimal. Since the amounts are nonnegative, any plan that ends before the final two houses in the range can also rob the last house in the range without reducing the total amount. Therefore, returning `max(ops)` gives the optimal value for the range.

For the circular problem, if an optimal plan does not rob houses `n - 1`, `0`, or `1`, house `0` can also be robbed without reducing the total amount. Therefore, there is always an optimal plan that includes at least one of these three houses.

The code enumerates these three cases, excludes the adjacent houses in each case, and solves the remaining range. Thus, the final maximum is the global optimal value.

# Complexity

- **Time Complexity:** `O(n)`. `maxValue` is called three times, and each call processes at most `O(n)` houses.
- **Auxiliary Space Complexity:** `O(1)`. The queue stores at most two states, and `dp` stores only three results. The slice used in the short-range branch contains at most two elements.