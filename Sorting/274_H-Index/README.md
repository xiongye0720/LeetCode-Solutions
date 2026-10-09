# Approach

First, find the maximum citation count `maxCite`, use `max(maxCite, len(citations))` as the initial upper bound, and use `citeDict` to count the papers for each citation count.

Then decrease the candidate value one by one, starting from the upper bound. Each time, add the number of papers with the current citation count to `Total`, so that it represents the number of papers with **at least the current `upBound` citations**. When `Total >= upBound`, return the current candidate value.

Since the initial upper bound is no smaller than the maximum citation count, the `item >= upBound` branch during counting can only handle citation counts equal to the upper bound.

# Correctness

The initial upper bound covers all citation counts. Each time the candidate value decreases, the number of papers with exactly that many citations is added. Therefore, before each check, `Total` accurately represents the number of papers with at least the current candidate value in citations.

`Total >= upBound` exactly satisfies the condition for the H-index. Since candidate values are checked in descending order, the first value that satisfies the condition is the largest valid H-index. If there is no positive answer, the loop will return when it reaches `0`.

# Complexity

Let the number of papers be `n` and the maximum citation count be `M`, assuming dictionary operations take O(1) on average:

- **Time complexity: O(n + M)**. The two traversals take O(n), and the descending checks run at most `max(n, M) + 1` times. Even if a citation count does not appear in the dictionary, that candidate value is still checked.
- **Space complexity: O(n)**. The dictionary stores at most `n` distinct citation counts.