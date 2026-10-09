# Approach

Use `wordQue` to store unprocessed words in their original order, taking words out to build the result one line at a time.

- **Greedy line grouping**: `rowLen` equals the total length of the current words plus the number of words, effectively reserving one space for each word. Therefore, `rowLen + len(temWord)` is exactly the line length after adding the next word with only one space between words. If it exceeds `maxWidth`, put the word back at the front of the queue and finish the current line.
- **Last line**: Join the words with one space, then pad the right side.
- **Non-last lines**: If there is only one word, pad the right side. Otherwise, distribute the remaining spaces among the gaps between words. `quot` is the base number of spaces per gap, and `rem` is the number of gaps on the left that need one extra space.

# Correctness

The queue always preserves the original order of unprocessed words. Each line keeps adding words until the next word no longer fits, so each line contains the maximum number of words that can fit.

For a non-last line, let the total word length be `temLen` and the number of gaps be `g`. Then:

`maxWidth - temLen = quot × g + rem`

The first `rem` gaps contain `quot + 1` spaces, and the remaining gaps contain `quot` spaces. This distributes the spaces as evenly as possible, with more spaces on the left. The remainder branch adds an extra `sep2` after the last word, which is then removed by `rstrip(' ')`, so the final line width is still exactly `maxWidth`.

The last line and lines containing only one word are padded on the right, satisfying the left-alignment requirement.

# Complexity

Let the number of words be `n`, the line width be `W = maxWidth`, and the number of output lines be `L`.

- **Time complexity: O(nW) in the worst case**. Queue operations and word traversal take O(n). The remainder branch concatenates strings one at a time, repeatedly copying the existing content. A line with `k` words can therefore take up to O(kW) time.
- **Auxiliary space complexity: O(n + W)**. The queue and the current line store word references, and constructing a line string requires O(W) space.
- **Output space complexity: O(LW)**.