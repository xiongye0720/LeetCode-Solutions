# Approach

Start from each cell that matches `word[0]` and use DFS to match the word. `lvl` represents the number of characters already matched along the current path, so the next character to find is `word[lvl]`.

After entering a cell, temporarily set it to `None` to prevent the current path from using it again. Then search in the four adjacent directions. Before returning, restore the cell to `word[lvl-1]`. When `lvl == maxLvl`, the entire word has been matched. Record the result through the shared `ans` flag and return early through each recursive level.

Before searching, count the occurrences of the first and last characters on the board. If the last character appears less often, reverse the word to start searching from the end with fewer candidate starting cells.

# Correctness

Each recursive step enters only an adjacent cell that matches the next target character, so the characters along the path always match a prefix of the word. The temporary marker ensures that no cell is used more than once in the same path.

After a failed search, restoring the cell allows other candidate paths to use it. Cells are also restored at each level when a successful search returns, so the search does not change the board's final contents. Exploring all valid starting cells and adjacent choices covers all possible matching paths.

Adjacency on the board is bidirectional. A path matches the original word if and only if the reversed path matches the reversed word, so reversing the word does not affect the result.

# Complexity

Let the board size be `m × n` and the word length be `L`.

- **Time complexity: `O(mn · 3^L)`.** At most `mn` starting cells are tried. The first step has at most four directions, and each subsequent step excludes at least the previously visited cell, leaving at most three directions. Counting the first and last character frequencies takes `O(mn)` time.
- **Space complexity: `O(L)`.** The recursion depth is at most `min(L, mn)`, and reversing the word requires at most `O(L)` additional space. Visited states are recorded directly on the board.