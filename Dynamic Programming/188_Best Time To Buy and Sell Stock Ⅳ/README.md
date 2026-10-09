# Approach

Update profits using the price difference between two consecutive days, while maintaining two types of states:

- **Current-day profit**: the maximum profit when the last transaction ends on the current day, under a given transaction limit.
- **Historical profit**: the maximum profit up to the previous day, under the same transaction limit.

These states are stored in the first and second entries of a tuple, respectively. Taking the tuple's `max` gives the maximum profit up to the current day.

The code allows a zero-profit transaction that buys and sells on the same day to represent fewer transactions. Both `prices[i-1]-prices[i-1]` and `prices[j-1]-prices[j-1]` equal `0`.

# Correctness

Let `Δ` be the price difference between the current day and the previous day. If the last transaction ends on the current day, there are two cases:

1. **Bought on an earlier day**: postpone the previous day's sale to the current day. The profit is “the previous day's current-day profit + Δ.”
2. **Bought on the current day**: this transaction earns a profit of `0`. The previous profit is “the maximum profit up to the current day with one fewer transaction.” When the transaction limit is one, this value is `0`.

Taking the maximum of the two gives the current-day profit. These cases cover all possible buying times. In the second case, the previous transaction sells no later than the current day, and the next purchase follows, so the holdings do not overlap.

Both branches use the same transition, but the array meanings and update orders differ:

- **`k <= n`**: iterate over days, with `dp[j]` representing the state for at most `j` transactions. During an update, the old `dp[j][0]` comes from the previous day, while the updated `max(dp[j-1])` comes from the current day. The second entry takes the old `max(dp[j])`, preserving the maximum profit up to the previous day.
- **`k > n`**: iterate over transaction counts, with `dp[j]` corresponding to the day at price index `j-1`. During an update, the updated `dp[j-1][0]` comes from the previous day under the current transaction limit, while the old `max(dp[j])` comes from the current day with one fewer transaction. The second entry takes the updated `max(dp[j-1])`, summarizing the profit up to the previous day under the current transaction limit.

Therefore, both traversal orders provide the correct states needed for the transition. Finally, `max(dp[-1])` combines the profits from at most `k` transactions ending on the last day or earlier, giving the answer.

# Complexity

Let `n` be the number of prices:

- Time complexity: `O(nk)`, since both branches iterate over combinations of days and transaction counts.
- Space complexity: `O(min(n,k))`, since the array length is either `k+1` or `n+1`, depending on the branch.