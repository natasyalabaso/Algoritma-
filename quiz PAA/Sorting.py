import time
import random

# Fungsi Bubble Sort
def bubble_sort(arr):
    """
    Mengurutkan array menggunakan Bubble Sort.
    Kompleksitas waktu: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Fungsi Merge Sort
def merge_sort(arr):
    """
    Mengurutkan array menggunakan Merge Sort.
    Kompleksitas waktu: O(n log n)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Fungsi Penggabungan untuk Merge Sort
def merge(left, right):
    """
    Menggabungkan dua array yang sudah terurut.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Tambahkan elemen yang tersisa
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Fungsi untuk mencatat waktu komputasi
def measure_time(sort_function, arr):
    """
    Mengukur waktu eksekusi sebuah fungsi sorting.
    """
    start = time.time()
    sorted_arr = sort_function(arr[:])  # Gunakan salinan array agar array asli tidak berubah
    end = time.time()
    return sorted_arr, end - start

# Dataset acak: X = random of 100 integer numbers
X = [random.randint(0, 10000) for _ in range(100)]

# Eksekusi algoritma dan pengukuran waktu
bubble_sorted, bubble_time = measure_time(bubble_sort, X)
merge_sorted, merge_time = measure_time(merge_sort, X)

# Output hasil
print("Data asli (10 data pertama):", X[:10])
print("\nBubble Sort (10 data pertama):", bubble_sorted[:10])
print(f"Waktu eksekusi Bubble Sort: {bubble_time:.6f} detik")

print("\nMerge Sort (10 data pertama):", merge_sorted[:10])
print(f"Waktu eksekusi Merge Sort: {merge_time:.6f} detik")
