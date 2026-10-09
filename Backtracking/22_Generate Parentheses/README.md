# Approach

The code uses DFS to add parentheses one at a time, extending only valid prefixes:

- `numOfPar` records the remaining counts of left and right parentheses.
- `lPar[0]` records the current number of unmatched left parentheses.
- `proc` stores the parenthesis sequence being constructed, and `tar` specifies whether to add a left or right parenthesis in the current call.

Each call first adds the specified parenthesis, then decides the next step:

- If there are no unmatched left parentheses, only a left parenthesis can be added.
- If there are unmatched left parentheses, a right parenthesis can be added. If any left parentheses remain, also explore the branch that adds a left parenthesis.
- When both types of parentheses are used up, save the result using `''.join(proc)`.

Before each call returns, restore the remaining counts, pop the parenthesis added in this call, and restore the unmatched count so that different branches do not affect each other.

# Correctness

The initial call adds a left parenthesis. After that, a right parenthesis is added only when `lPar[0] > 0`, so no prefix contains more right parentheses than left parentheses.

The following always holds:

`lPar[0] = numOfPar[1] - numOfPar[0]`

Therefore, whenever there are unmatched left parentheses, there must be right parentheses remaining. If the unmatched count is zero and the sequence is not yet complete, there must be left parentheses remaining. Thus, the branches in the code never use a type of parenthesis that has already been exhausted.

When both types of parentheses are used up, the sequence contains `n` left parentheses and `n` right parentheses, and every prefix is valid, so the saved sequence is valid. The code explores all valid choices for each prefix, and each complete sequence corresponds to a unique choice path, so no results are missed or duplicated.