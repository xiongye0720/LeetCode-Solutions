# Approach and Correctness

First, calculate the total skill sum `total` and count the occurrences of each skill value in `freq`. The number of teams is `cnt`, so the skill sum of each team must be `total // cnt`. If `total` is not divisible by `cnt`, return `-1` immediately. Therefore, `teamSums` has at most one candidate value.

For the candidate skill sum `item`, a skill value `key` can only be paired with `item-key`:

- If the complementary skill value does not exist, pairing is impossible.
- If the two skill values are different, their occurrence counts must be equal.
- If the two skill values are the same, the occurrence count must be even.

These conditions are both necessary and sufficient: different skill values can be paired one by one with equal counts, and identical skill values can be paired in twos, using all players exactly once.

After validation, accumulate `key * (teamSum-key) * freq[key]`. Each player contributes the skill product of their team once, so each team is counted twice. Finally, return `ans // 2`.

# Complexity

Let the number of players be `n`, and let the number of distinct skill values be `k`.

- **Time Complexity:** `O(n)` on average. Counting frequencies takes `O(n)`, while validating the pairs and calculating the answer each take `O(k)`. Hash table operations take `O(1)` on average.
- **Auxiliary Space Complexity:** `O(k)`. The frequency dictionary stores the distinct skill values, `nums` only references the original list, and `teamSums` stores at most one element.