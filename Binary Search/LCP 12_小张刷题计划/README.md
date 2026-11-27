# Approach and Correctness

Each day, asking for help saves the time needed for one problem, so the minimum actual time for a consecutive block of problems that day is `temSum - temMax`. The code uses binary search on the daily time limit.

For a candidate limit `mid`, the code completes the longest feasible prefix of the remaining problems each day. The first problem that would exceed the limit is left for the next day and processed again using `ptr = temPtr`. Completing as many problems as possible today leaves a shorter suffix for later days. Removing a prefix cannot increase the actual time needed for a block of problems, so this partition gives the minimum number of days needed, `daysUsed`.

If the number of problems is at most `dayCnt`, each problem can be assigned its own day and solved with help, so the answer is `0`. Otherwise, since every problem takes positive time, `left = 0` is infeasible. The limit `right = totalTime - maxTime` is enough to complete all problems in one day, so it is feasible.

Increasing the limit cannot increase the number of days needed, so feasibility can be checked using `daysUsed ≤ dayCnt`. Binary search keeps the left endpoint infeasible and the right endpoint feasible. When the endpoints are adjacent, the code returns `right`, the smallest feasible limit.

# Complexity

Let `n` be the number of problems and `U = totalTime - maxTime` be the initial upper bound for binary search.

- **Time Complexity:** `O(n + n log(U + 1))`. Preprocessing scans the array once. In each feasibility check, a problem is examined at most twice, once when it causes the limit to be exceeded and once when it is processed again the next day. Each check therefore takes `O(n)` time.
- **Auxiliary Space Complexity:** `O(1)`. Only a fixed number of variables are used, and `times` directly references the original array.