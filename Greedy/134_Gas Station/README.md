# Approach

Start from the candidate starting station `left`, use `total` to track the remaining fuel, and use `temPtr % length` to access stations along the circular route.

- At each station, add `gas - cost` to the remaining fuel.
- If the remaining fuel becomes negative, the current starting station fails, and the next candidate starting station is set to `temPtr + 1`.
- If `length` consecutive stations are visited and the remaining fuel stays nonnegative throughout, a full circuit can be completed, so return `left`.
- After all candidate starting stations have been ruled out, return `-1`.

# Correctness

The key point is: **When starting from `left` and failing for the first time at `temPtr`, all starting stations between them can be ruled out.**

Let the failure position be `k`. The cumulative net fuel from `left` to `k` is negative, while the cumulative net fuel up to every earlier position is nonnegative.

For any `left < j <= k`, the cumulative net fuel from `j` to `k` equals:

`the cumulative value from left to k − the cumulative value from left to j-1`

The result must be negative. Therefore, starting from `j` also cannot get through this section of the route, so we can skip directly to `k + 1`. When access wraps around the circular route, this reasoning still applies to starting stations that have not yet been ruled out.

Thus, none of the skipped starting stations can succeed, and any returned starting station has passed the check for a full circuit.

# Complexity

Let the number of stations be `n`:

- **Time complexity: O(n)**. Using indices before applying the modulo operation, each failed attempt continues from the station immediately after the failure position, so previously checked positions are not checked again; the final attempt visits at most one more full circuit, making the total number of checks less than `2n`.
- **Space complexity: O(1)**, since only a fixed number of variables are used.