from typing import List

def insertion_sort(lst: List[int]) -> List[int]:
    result: List[int] = []

    for value in lst:
        inserted = False
        for index in range(len(result)):
            if value < result[index]:
                result.insert(index, value)
                inserted = True
                break
        if not inserted:
            result.append(value)

    return result

def selection_sort(lst: List[int]) -> List[int]:
    result = lst.copy()
    for i in range(len(result)):
        min_idx = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result

def bubble_sort(lst: List[int]) -> List[int]:
    result = lst.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
