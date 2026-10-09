# Approach

Remove duplicates from `nums` and sort the distinct values, assigning an ID to each value. The IDs preserve the order of the values, so querying values smaller than the current value is equivalent to querying the range of smaller IDs.

The segment tree maintains, for each ID, **the length of the longest increasing subsequence ending with the corresponding value among the processed elements**. Internal nodes store the maximum value in their intervals, and `-1` indicates that no valid record exists yet.

When processing `nums[i]`:

- `plan1`: the length of the longest increasing subsequence ending at the current element. Query the ID range `[0, numToId[nums[i]] - 1]` and add one to the result. If the range is empty or has no records, use `1`.
- `plan2`: the length of the longest increasing subsequence among all previous elements, which is the maximum of the two components in the previous `dp` entry.

Then update the segment tree position for the current value using `plan1`, and store `dp[i] = (plan1, plan2)`. The maximum of the two components in the final entry is the answer.

# Correctness

For any increasing subsequence of length greater than one ending at the current element, the preceding element must appear earlier and have a strictly smaller value. The segment tree query covers all such ending values. Taking the maximum length among them and adding one gives the optimal `plan1`.

The query occurs before the update and excludes the current ID, so it neither uses the current element itself nor connects equal elements.

For the same value, only the maximum subsequence length needs to be retained, because whether a later element can follow it depends only on the value. The maximum operation in `UpdNode` maintains this property.

The optimal subsequence in each prefix either ends at the current element or lies entirely among the previous elements, so `max(plan1, plan2)` correctly gives the answer for that prefix.

# Complexity

Let `n` be the length of the array and `k` be the number of distinct values.

- **Time complexity: `O(n log(k + 1))`.** Removing duplicates and sorting takes `O(n + k log k)` time. Each element requires at most one range query and one point update.
- **Space complexity: `O(n + k)`.** `dp` stores `n` entries, the ID mapping and segment tree use `O(k)` space, and the recursion stack uses `O(log(k + 1))` space.