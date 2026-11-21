# Approach and Correctness

The code uses `tripDict` to group trips by pickup location and sorts the unique pickup locations in `starts` in ascending order. The min-heap `ops` stores trips that have not yet ended, with the earliest drop-off location at the top.

When processing a pickup location `item`, the code first pops all trips whose drop-off locations are at or before `item` and subtracts their passenger counts from `passCnt`. It then adds all trips starting at the current location. This ensures that passengers get off before others get on at the same location, so `passCnt` after processing is the actual number of passengers in the car.

Between two adjacent pickup locations, the passenger count can only decrease as passengers get off. Therefore, the maximum passenger count must occur just after a pickup location has been processed. `maxCnt` records the maximum passenger count at these locations, and the code finally checks whether it exceeds `capacity`.

# Complexity

Let `n` be the number of trips.

- **Time Complexity:** `O(n log n)`. Sorting the pickup locations takes at most `O(n log n)`. Each trip is pushed onto the heap once and popped at most once. Dictionary and set operations take `O(1)` time on average.
- **Auxiliary Space Complexity:** `O(n)`. The space is used for grouping trips, storing pickup locations, and maintaining the min-heap.