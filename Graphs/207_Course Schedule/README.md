# Approach

Treat courses as nodes. Each prerequisite pair `[a, b]` corresponds to a directed edge `b → a`.

- `courses[b]` stores the subsequent courses that depend on course `b`.
- `inDegree[a]` records the number of prerequisites for course `a` that have not yet been completed.
- Initially, add all courses with an in-degree of zero to `ops`.

The code processes available courses in batches: take a course from `ops`, increment the completed course count `cnt`, and decrease the in-degrees of its subsequent courses. Courses whose in-degrees drop to zero are added to `temOps` for the next batch.

After the queues are exhausted, check `cnt == numCourses` to determine whether all courses have been completed.

# Correctness

The in-degree always represents the number of prerequisite dependencies that have not yet been processed, so a course is enqueued only after all its prerequisites have been completed. Each course is enqueued at most once, and the processing order satisfies all dependencies.

If the graph contains a cycle, each course in the cycle always retains at least one dependency from within the cycle and cannot be enqueued. Therefore, fewer than all courses are completed.

If the graph has no cycles, every nonempty remaining graph has a node with an in-degree of zero, so processing can continue until all courses are completed. Therefore, `cnt == numCourses` holds if and only if all courses can be completed.

# Complexity

Let `V` be the number of courses and `E` be the number of prerequisite relationships.

- **Time complexity:** `O(V + E)`, since each course is processed at most once and each dependency is traversed at most once.
- **Space complexity:** `O(V + E)`, for the adjacency list, in-degree array, and two queues.