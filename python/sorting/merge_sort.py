#!/usr/bin/python3
import random


def merge_sort(lst):
    if len(lst) <= 1:
        return lst;

    pivot = len(lst) // 2

    left = lst[:pivot]
    right = lst[pivot:]

    merge_sort(left)
    merge_sort(right)    

    idx_l = idx_r = 0
    lst.clear()

    while (idx_l < len(left)) and (idx_r < len(right)):
        if left[idx_l] <= right[idx_r]:
            lst.append(left[idx_l])
            idx_l = idx_l + 1
        else:
            lst.append(right[idx_r])
            idx_r = idx_r + 1

    if idx_l < len(left):
        lst.extend(left[idx_l:])
    if idx_r < len(right):
        lst.extend(right[idx_r:])


def main():
    sz = random.randint(2, 20)
    data = []

    for i in range(sz):
        data.append(random.randint(0, 100))
    
    print(f"Original list...", end=": ")
    print(*data, sep=", ")

    merge_sort(data)

    print(f"Sorted list....", end=": ")
    print(*data, sep=", ")


if __name__ == "__main__":
    main()

