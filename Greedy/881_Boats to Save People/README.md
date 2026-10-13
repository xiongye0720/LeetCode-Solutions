# Approach

Divide the weights using `threshold = (info[0]//2) + 1`:

- Everyone in `high` weighs more than half the weight limit, so no two of them can share a boat.
- Everyone in `low` weighs at most half the weight limit, so any two of them can share a boat.

Sort `high` in descending order and `low` in ascending order. Each time, remove the heaviest person from `high` and count one boat for them. If they can share a boat with the lightest person in `low`, remove that person from `low` as well.

This choice does not increase the number of boats: if even the lightest person cannot share a boat with the current heaviest person, no other person in `low` can pair with them either. If they can pair, existing pairs can be rearranged to put them in the same boat. The displaced person from `low` can still share a boat with a lighter person from `high` or another person from `low`, so no pairing opportunities are lost.

Each remaining person in `high` needs one boat. The remaining people in `low` can be paired arbitrarily, requiring `(len(low)+1)//2` boats. Therefore, `cnt` is the minimum number of boats needed.

# Complexity

Let the number of people be `n`.

- **Time Complexity:** `O(n log n)`. Grouping and queue processing both take `O(n)`, and the main cost comes from sorting the two groups.
- **Auxiliary Space Complexity:** `O(n)`. This is used for the group lists, deques, and temporary space for sorting.