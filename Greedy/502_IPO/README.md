# Approach

In each round, the code selects the project with the highest profit among those that can be started with the current capital.

- `proj` groups project profits by their required starting capital, and `caps` stores the distinct capital requirements in ascending order.
- `ptr` points to the first capital threshold whose projects have not yet been added to the heap. In each round, all projects with thresholds no greater than `w` are added to `ops`, and the pointer is advanced.
- `ops` stores negative profits, allowing a min-heap to retrieve the maximum profit. This profit is added to `w`, and the remaining project allowance is decreased by one.
- The process ends when the allowance is exhausted or the heap is empty.

The starting capital is only a requirement for executing a project and is not deducted. After a project is completed, the capital increases by that project's profit.

# Correctness

The problem guarantees nonnegative profits, so `w` never decreases, and projects whose capital requirements have already been met remain available. After projects are added in each round, the heap contains exactly all projects that can be executed and have not yet been completed. The pointer only moves forward, each project enters the heap once, and a project is never executed again after being removed.

Let `A` be the project with the highest profit currently available, and suppose an optimal solution first chooses project `B`. If that solution includes `A` later, we can move `A` to the beginning and place `B` in `A`'s original position: capital does not decrease during the exchange, and the capital is the same afterward. If the solution does not include `A`, replacing `B` with `A` also does not decrease the capital available for later projects. Therefore, there is always an optimal solution that starts with `A`, and choosing the highest-profit project in each round produces an optimal result.

If the heap is empty, every unfinished project requires more capital than is currently available. The capital cannot increase further, so the process can end.

# Complexity

Let the number of projects be `n`.

- **Time complexity:** `O(n log n)`. Grouping takes `O(n)`, and sorting the thresholds takes at most `O(n log n)`; each project enters the heap at most once, and the total number of heap removals is at most `min(k, n)`.
- **Space complexity:** `O(n)`, for the grouping dictionary, threshold list, and heap.