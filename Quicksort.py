import random
import time
import sys

# Increase recursion limit safely
sys.setrecursionlimit(10000)

# ---------------------------------------------
# Optimized Deterministic Quicksort
# ---------------------------------------------
def quicksort(arr):
    """Performs deterministic quicksort using last element as pivot (tail-recursion optimized)."""
    def _quicksort(arr, low, high):
        while low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            p = i + 1
            # Recurse on smaller half to avoid deep recursion
            if p - low < high - p:
                _quicksort(arr, low, p - 1)
                low = p + 1
            else:
                _quicksort(arr, p + 1, high)
                high = p - 1

    _arr = arr.copy()
    _quicksort(_arr, 0, len(_arr) - 1)
    return _arr

# ---------------------------------------------
# Optimized Randomized Quicksort
# ---------------------------------------------
def randomized_quicksort(arr):
    """Performs randomized quicksort by randomly selecting a pivot."""
    def _randomized_quicksort(arr, low, high):
        while low < high:
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            p = i + 1
            if p - low < high - p:
                _randomized_quicksort(arr, low, p - 1)
                low = p + 1
            else:
                _randomized_quicksort(arr, p + 1, high)
                high = p - 1

    _arr = arr.copy()
    _randomized_quicksort(_arr, 0, len(_arr) - 1)
    return _arr

# ---------------------------------------------
# Utility Functions
# ---------------------------------------------
def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

def generate_inputs(size):
    random_list = [random.randint(0, 10000) for _ in range(size)]
    sorted_list = sorted(random_list)
    reverse_sorted_list = sorted(random_list, reverse=True)
    return random_list, sorted_list, reverse_sorted_list

# ---------------------------------------------
# Main Demonstration
# ---------------------------------------------
if __name__ == "__main__":
    print("=== Quicksort Assignment ===\n")

    # Demonstrate correctness
    sample = [42, 15, 73, 8, 91, 27, 50]
    print("Original array:", sample)
    print("Deterministic Quicksort:", quicksort(sample))
    print("Randomized Quicksort:", randomized_quicksort(sample))
    print("\n---------------------------------------------\n")

    # Performance comparison
    sizes = [1000, 5000, 10000]
    for n in sizes:
        rand_list, sorted_list, rev_sorted = generate_inputs(n)
        print(f"Input size: {n}")
        print("Random input:")
        print(f"  Deterministic Quicksort: {measure_time(quicksort, rand_list):.5f}s")
        print(f"  Randomized Quicksort:    {measure_time(randomized_quicksort, rand_list):.5f}s")

        print("Sorted input (worst case for deterministic):")
        print(f"  Deterministic Quicksort: {measure_time(quicksort, sorted_list):.5f}s")
        print(f"  Randomized Quicksort:    {measure_time(randomized_quicksort, sorted_list):.5f}s")

        print("Reverse-sorted input:")
        print(f"  Deterministic Quicksort: {measure_time(quicksort, rev_sorted):.5f}s")
        print(f"  Randomized Quicksort:    {measure_time(randomized_quicksort, rev_sorted):.5f}s")
        print("---------------------------------------------")
