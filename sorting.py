# MergeSort(arr[], l, r):
#     if l < r:
#         mid = (l + r) // 2
#         MergeSort(arr, l, mid)
#         MergeSort(arr, mid + 1, r)
#         Merge(arr, l, mid, r)
# Merge(arr[], l, mid, r):
#     Create temporary arrays L[] and R[]
#     Copy data into L[] and R[]
#     Merge L[] and R[] back into arr[l..r]

# Penjelasan Merge Sort : Merge Sort memiliki kompleksitas waktu Big O (O(n log n)) dalam kasus terbaik, rata-rata, dan terburuk, karena proses pembagian array menjadi subarray (logaritmik) dan penggabungan kembali (linear) dilakukan secara rekursif. Analisis Big Theta (Θ(n log n)) juga menunjukkan bahwa jumlah langkah minimum untuk Merge Sort adalah sebanding dengan jumlah operasi pembagian dan penggabungan, menjadikannya algoritma yang sangat efisien untuk dataset besar dan terurut secara acak. Namun, kompleksitas ruangnya adalah O(n) karena membutuhkan ruang tambahan untuk menyimpan subarray sementara, menjadikannya kurang optimal dalam hal penggunaan memori dibanding algoritma in-place.

# BubbleSort(arr[], n):
#     for i = 0 to n-1:
#         for j = 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                 Swap arr[j] and arr[j+1]

# Penjelasan Bubble Sort : Bubble Sort memiliki kompleksitas waktu Big O (O(n²)) dalam kasus rata-rata dan terburuk, karena setiap elemen dibandingkan dan ditukar dengan elemen lainnya dalam iterasi bertingkat. Dalam kasus terbaik, ketika array sudah terurut, kompleksitas waktu Big O (O(n)) terjadi karena hanya membutuhkan satu iterasi untuk memverifikasi urutan elemen. Big Theta (Θ(n²)) menunjukkan jumlah operasi yang harus dilakukan rata-rata, menjadikannya algoritma yang sangat tidak efisien untuk dataset besar. Keunggulan Bubble Sort terletak pada penggunaan memori yang minimal (O(1)), tetapi kecepatan lambat membuatnya jarang digunakan dalam praktik nyata.


import random
import time

# Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Implementasi Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Generate data random
arr = [random.randint(0, 1000) for _ in range(100)]
arr_bubble = arr[:]
arr_merge = arr[:]

# Mengukur waktu Bubble Sort
start_time_bubble_sort = time.perf_counter()
bubble_sort(arr_bubble)
end_time_bubble_sort = time.perf_counter()
time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

# Mengukur waktu Merge Sort
start_time_merge_sort = time.perf_counter()
merge_sort(arr_merge)
end_time_merge_sort = time.perf_counter()
time_complexity_merge = end_time_merge_sort - start_time_merge_sort

# Menampilkan hasil
print(f"Hasil perhitungan dari Bubble Sort adalah sebagai berikut: {arr_bubble[:10]} ...\n")
print(f"Hasil perhitungan dari Merge Sort adalah sebagai berikut: {arr_merge[:10]} ...\n")
print(f"Time Complexity untuk Bubble Sort: {time_complexity_bubble:.10f} detik\n")
print(f"Time Complexity untuk Merge Sort: {time_complexity_merge:.10f} detik\n")
