
import time
import matplotlib.pyplot as plt
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort

# Arrays
arr1 = list(range(1, 6))
arr2 = list(range(1, 11))
arr3 = list(range(1, 51))
arr4 = list(range(1, 101))
arrays = [arr1, arr2, arr3, arr4]
input_sizes = [len(arr1), len(arr2), len(arr3), len(arr4)]

# Sorting algorithms
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort
}

# Record average times
results = {name: [] for name in algorithms.keys()}

for name, func in algorithms.items():
    for arr in arrays:
        times = []
        for _ in range(5):
            temp = arr.copy()
            start = time.perf_counter()
            func(temp)
            end = time.perf_counter()
            times.append((end - start) * 1000) # milliseconds
        avg_time = sum(times) / len(times)
        results[name].append(avg_time)

# Plotting
for name, times in results.items():
    plt.plot(input_sizes, times, marker='o', label=name)

plt.xlabel('Input Size (N)')
plt.ylabel('Average Execution Time (ms)')
plt.title('Sorting Algorithm Time Analysis')
plt.legend()
plt.grid(True)
plt.savefig('graph.png')
plt.show()

# Print Table
print("\n--- Average Execution Times (ms) ---")
print(f"{'Input Size':<10} {'Bubble':<10} {'Selection':<10} {'Insertion':<10} {'Merge':<10}")
for i in range(len(input_sizes)):
    print(f"{input_sizes[i]:<10} {results['Bubble Sort'][i]:<10.4f} {results['Selection Sort'][i]:<10.4f} {results['Insertion Sort'][i]:<10.4f} {results['Merge Sort'][i]:<10.4f}")
