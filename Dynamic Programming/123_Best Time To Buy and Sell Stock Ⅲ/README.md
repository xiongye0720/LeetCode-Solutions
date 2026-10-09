# Approach

The code maintains only two tuples: `dp[0]` corresponds to at most one transaction, and `dp[1]` corresponds to at most two transactions. After each iteration's updates:

- The first entry: the maximum profit when the last transaction ends on the current day.
- The second entry: the maximum profit over previous days, excluding the current day.

A zero-profit transaction that buys and sells on the same day is allowed as a placeholder, so the states can also represent fewer transactions. `max(dp[k])` is the maximum profit up to the current day with at most `k+1` transactions.

# Correctness

Let the price difference between the current day and the previous day be:
`Δ = prices[j-1] - prices[j-2]`

For at most one transaction, a transaction ending on the current day has two possible cases:

- Extend the previous day's transaction by postponing the sale by one day, increasing the profit by `Δ`.
- Buy and sell on the current day, earning a profit of `0`.

Therefore, the update is `max(dp[0][0] + Δ, 0)`.

For at most two transactions, there are also two cases:

- Extend the previous day's last transaction, obtaining `dp[1][0] + Δ`.
- Start a zero-profit transaction on the current day, using the updated `max(dp[0])` as the previous profit.

Using the current day's maximum profit from at most one transaction in the second case is valid: the previous transaction sells no later than the current day, and the next transaction buys afterward on the same day, so the two transactions do not hold stocks at the same time. The zero-profit transaction can also be omitted, so the transaction limit is not exceeded.

These two cases cover all possibilities in which the last transaction ends on the current day. The second tuple entry uses `max` to retain the maximum profit from the old state. The `max(dp[k])` on the right-hand side of the assignment reads the tuple before the update, so it summarizes the results up to the previous day.

Finally, `max(dp[1])` considers transactions ending on the current day as well as those ending earlier, giving the maximum profit with at most two transactions.

# Complexity

Let `n` be the number of prices:

- Time complexity: `O(n)`, since each day requires only a constant number of calculations.
- Space complexity: `O(1)`, since only two fixed-size tuples are stored.