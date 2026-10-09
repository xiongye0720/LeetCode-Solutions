# Approach

`dp[i] = (P, Q)` represents the following state using the coins processed so far:

- `P` is the maximum amount that can be formed without exceeding `i`.
- `Q` is the minimum number of coins needed to form amount `P`.

All states are initially `(0, 0)`, representing the use of no coins.

For each denomination `item`, iterate over capacities `i` in increasing order. Add one coin of the current denomination to `dp[i-item]` to obtain a candidate state:

```text
plan2P = dp[i-item][0] + item
plan2Q = dp[i-item][1] + 1
```

Prefer the state with the larger amount. If the amounts are equal, choose the state with fewer coins. Since capacities are processed in increasing order, `dp[i-item]` may already use the current coin, allowing each denomination to be used multiple times.

# Correctness

For capacity `i`, the optimal solution either uses no coins of the current denomination and keeps the original `dp[i]`, or uses at least one current coin. After removing one such coin, the remaining amount does not exceed `i-item`.

Adding the same coin increases every amount by `item` and every coin count by `1`, so it preserves the ordering that prioritizes the amount first and the coin count second. Therefore, using the optimal state in `dp[i-item]` gives the optimal candidate that includes the current coin.

Finally, if `dp[amount][0] == amount`, the second component is the minimum number of coins needed to form the target amount exactly. Otherwise, the maximum amount that can be formed is still smaller than the target, so no solution exists.

# Complexity

Let `k` be the number of coin denominations and `A` be the target amount.

- **Time complexity: `O(k(A + 1))`.** Each denomination iterates over at most all amount states.
- **Space complexity: `O(A + 1)`.** The dynamic programming array contains `A + 1` two-element tuples.