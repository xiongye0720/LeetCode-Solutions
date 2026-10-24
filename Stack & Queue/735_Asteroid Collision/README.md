# Approach

At the end of each iteration, `ans` stores the negative values confirmed to survive, and `stack` stores the currently surviving positive values. Both preserve their original order.

When a positive value is encountered, push it directly onto `stack`. When a negative value is encountered, push it onto the stack first, then use a loop to handle collisions with the preceding positive values one by one:

- `temPos + temNeg == 0`: both disappear.
- `temPos > -temNeg`: the positive value survives. Push it back onto the stack and end the current round of collisions.
- Otherwise: the negative value survives. Push it back onto the stack and continue colliding with earlier positive values.

If no positive value remains to the left of the negative value, add it to `ans`. Finally, return `ans + stack`.

# Correctness

A collision can only occur between an asteroid on the left moving right and an asteroid on the right moving left.

The first asteroid a new negative value encounters must be the positive value at the top of the stack, so processing from the top follows the actual collision order. Each collision determines the survivor based on absolute values. If the negative value survives, continue to the next collision until it disappears or no positive value remains to its left.

Negative values added to `ans` will never collide with later asteroids, and the remaining positive values will not collide with one another. Therefore, the final survivors appear exactly in the order of `ans` followed by `stack`.

# Complexity

Let the number of asteroids be `n`.

- **Time Complexity:** `O(n)`. Each collision destroys at least one asteroid, so the total number of collisions is `O(n)`. The remaining traversal, stack pushes, and result concatenation also take `O(n)` in total.
- **Auxiliary Space Complexity:** `O(n)`. `ans` and `stack` together store at most `n` elements. The returned list created by concatenation uses an additional `O(n)` space.