import random
import time

import pandas as pd
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_sort_time(sort_function, arr, repeats=5):

    total_time = 0

    for _ in range(repeats):

        arr_copy = arr.copy()

        start_time = time.perf_counter()
        sort_function(arr_copy)
        total_time += time.perf_counter() - start_time

    return total_time / repeats

array_sizes = [10_000, 50_000, 100_000, 500_000]

results = []

for size in array_sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    randomized_time = measure_sort_time(randomized_quick_sort, arr)
    deterministic_time = measure_sort_time(deterministic_quick_sort, arr)

    print(f"Array size: {size}")
    print(f"Randomized Quick Sort Time: {randomized_time:.6f} seconds")
    print(f"Deterministic Quick Sort Time: {deterministic_time:.6f} seconds")
    results.append({
        "size": size,
        "randomized_time": randomized_time,
        "deterministic_time": deterministic_time
    })

results_df = pd.DataFrame(results)

results_df.columns = [
    "Array Size",
    "Randomized QuickSort",
    "Deterministic QuickSort"
]

print("\nResults table:")
print(results_df.to_string(index=False))

plt.plot(
    results_df["Array Size"],
    results_df["Randomized QuickSort"],
    marker="o",
    label="Randomized QuickSort"
)

plt.plot(
    results_df["Array Size"],
    results_df["Deterministic QuickSort"],
    marker="o",
    label="Deterministic QuickSort"
)

plt.xlabel("Array Size")
plt.ylabel("Average Time (seconds)")
plt.title("QuickSort Performance Comparison")
plt.legend()
plt.grid(True)

plt.savefig("quicksort_comparison.png", dpi=300, bbox_inches="tight")
plt.show()