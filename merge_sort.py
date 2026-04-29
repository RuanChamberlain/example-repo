def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively split
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge while comparing string lengths
        while i < len(left_half) and j < len(right_half):
            if len(left_half[i]) > len(right_half[j]):  # 🔥 key change
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# ----------- TEST LISTS -----------

list1 = ["apple", "banana", "kiwi", "watermelon", "grape", "pineapple", "pear", "mango", "blueberry", "plum"]

list2 = ["cat", "elephant", "dog", "hippopotamus", "lion", "tiger", "giraffe", "zebra", "cheetah", "leopard"]

list3 = ["python", "java", "javascript", "c", "cplusplus", "ruby", "go", "swift", "kotlin", "typescript"]


# ----------- RUN TESTS -----------

for i, lst in enumerate([list1, list2, list3], start=1):
    print(f"\nOriginal list {i}:")
    print(lst)

    merge_sort(lst)

    print(f"Sorted list {i} (longest → shortest):")
    print(lst)