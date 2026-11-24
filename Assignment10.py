import numpy as np

arr = np.arange(1, 11)
print("Original array (1 to 10):", arr)

print("First 4 elements (arr[:4]):", arr[:4])
print("Elements from index 3 to 7 (arr[3:8]):", arr[3:8])
print("Every second element (arr[::2]):", arr[::2])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

broadcast_arr = arr * 10 + 5
print("Broadcasted array (arr * 10 + 5):", broadcast_arr)