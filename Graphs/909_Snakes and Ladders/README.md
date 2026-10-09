# Approach

The code treats one dice roll and any resulting snake or ladder jump as one step, and uses level-order BFS to find the minimum number of steps.

**Coordinate conversion:** For a square number `nums`, `(nums-1)//n` is the row number counted from the bottom, so the actual row index is `n-1-(nums-1)//n`. Counting from the bottom, even-numbered rows run from left to right, and odd-numbered rows run from right to left. The column index is calculated accordingly.

**State expansion:** From the current square number, enumerate up to six landing squares ahead:

- If the cell value is `-1`, this square number is the final position for the step.
- If there is a snake or ladder, the final position for the step is the square number stored in the cell. Do not trigger another jump at that destination.

`visited` records the final position of each step. Mark positions when they are enqueued to avoid expanding them repeatedly.

**Level counting:** `ops` stores the current level, and `temOps` stores the next level. In each round, increment `cnt` and then expand the entire level. If the destination has entered `visited`, return `cnt`. If the queues are exhausted without reaching it, return `-1`.

# Correctness

The coordinate conversion follows the board's numbering rule, starting from the bottom-left corner and alternating direction on each row. Each expansion enumerates all valid dice landing squares and performs only one snake or ladder jump, so the state transitions follow the problem's rules.

Each transition corresponds to one dice roll. BFS expands states in increasing order of the number of rolls, so a position is first visited using the minimum number of rolls. The choices available from the same position are always identical, so skipping repeated visits cannot miss a shorter path.

Therefore, `cnt` when the destination first enters `visited` is the minimum number of rolls. If the search is exhausted, the destination is unreachable.

# Complexity

Let `n` be the side length of the board.

- **Time complexity:** `O(n²)`, since at most `n²` positions are expanded, and each position checks at most six landing squares.
- **Space complexity:** `O(n²)`, for the visited set and two queues.