# Approach

The code uses in-degree-based topological sorting.

For each prerequisite pair `[a, b]`, create a directed edge `b → a`. `gNode` stores the subsequent courses for each course, and `inDegree` records the number of prerequisites that have not yet been processed.

First, add all courses with an in-degree of zero to `ops`. Each time a course is dequeued, append it to `ans` and decrease the in-degree of each subsequent course by one. Courses whose in-degrees drop to zero are added to `temOps` for processing in the next round.

Finally, if `ans` contains all courses, return this order. Otherwise, return an empty list.

# Correctness

A course can be enqueued only when its in-degree is zero. At that point, all its prerequisites have been processed and added to `ans`, so the resulting order satisfies the prerequisite requirements. Each course is enqueued only once, when its in-degree reaches zero, so it is not added to the result more than once.

If the graph has no cycles, every nonempty remaining subgraph has a course with an in-degree of zero, so all courses can be processed. If a cycle exists, the courses in the cycle retain dependencies from within the cycle and cannot be enqueued. The final length of `ans` is therefore less than `numCourses`.

# Complexity

Let `V` be the number of courses and `E` be the number of prerequisite relationships.

- **Time complexity:** `O(V+E)`. Each course is processed at most once, and each prerequisite relationship is traversed at most once.
- **Space complexity:** `O(V+E)`. The adjacency list uses `O(V+E)` space, while the in-degree array, queues, and result list use `O(V)` space.