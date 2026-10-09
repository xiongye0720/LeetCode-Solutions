# Approach

`Left` represents the current position that is actually reachable.

If the last position has already been reached, return `True`; if the jump length at the current position is zero, return `False`; if a jump can go beyond the end of the array, a shorter jump can also reach the end, so return `True`.

Otherwise, among all positions reachable with one jump from the current position, choose the landing position that allows the next jump to reach the farthest:

- `TemEnd` is fixed as the rightmost reachable position in this round.
- `Tem` stores the “candidate landing position and the farthest position reachable from it,” with `TemEnd` as the initial candidate.
- Scan the remaining landing positions and update the candidate only when the farthest reachable position is strictly greater. Finally, move `Left` to the selected landing position.

# Correctness

Each selected landing position is within the current jump range, so `Left` always remains reachable and moves strictly to the right.

Let the selected landing position be `p`, and let the farthest position reachable from it be `R`. Since it has the farthest reachable endpoint among all candidates:

- Every other candidate to the right of `p` is at or before `R` and can be reached directly from `p`.
- Every other candidate to the left of `p` also has a reachable endpoint at or before `R`. For any path that passes through these positions and continues to the right, the first jump that reaches or passes `p` lands within `[p, R]`, so the same path can be followed from `p` onward.

Therefore, choosing `p` does not lose the opportunity to reach the end. If the jump length at the selected position is zero, the other candidates cannot jump past it either, so returning `False` is correct.

# Complexity

Let the array length be `n`.

- **Time complexity: O(n)**. The scanned intervals may overlap, but each position is scanned by the inner loop at most twice. Let the right boundary of the current round be `b`, and let the reachable endpoint of the selected position be `R`. Then the reachable endpoints of all candidates in this round are at or before `R`. In the next round, the default candidate is at `R`, and its reachable endpoint is at least `R`, so positions scanned in the current round cannot strictly improve upon that candidate. Therefore, the position selected in the next round is at least `b`, making the scanned intervals of rounds two apart non-overlapping.
- **Space complexity: O(1)**. Only a fixed number of variables are used.