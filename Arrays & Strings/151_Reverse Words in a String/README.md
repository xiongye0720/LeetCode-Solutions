# Approach

The code first converts the string into a character list `sList`, then processes it in two steps.

**1. Compress spaces**

When a space is encountered, `right` finds the start of the next word, and `wordR` finds the end of that word:

- If `left == 0`, move the word to the beginning of the list to remove leading spaces.
- If `right-left > 1`, move the word to `left+1`, keeping only one separating space.
- If there is already exactly one space between words, skip directly past the word.
- If there are no more words, set `endStr` to `left-1` to remove trailing spaces.

Characters are moved from left to right, and each destination position is always before its source position, so unread characters are not overwritten. After each move, the source position is set to a space to allow processing to continue. Finally, use a slice to keep the valid portion.

**2. Reverse the word order**

`reverseStr` reverses a specified range by swapping characters at its two ends. First, reverse the entire valid list, then reverse each word individually, and finally join the list into a string.

Compressing spaces preserves the original word contents and order. Reversing the entire list reverses both the word order and the character order within each word. Reversing each word restores its internal character order, so the final result has the words in reverse order with only one space between them.

# Complexity

Let the original string length be `n`:

- Time complexity: `O(n)`. Each pointer moves in one direction, and each word is scanned, moved, and reversed only a constant number of times.
- Space complexity: `O(n)`, for the character list, the slice, and the result string.