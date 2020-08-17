#!/usr/bin/python3
import random


def select_sort(lst):

    for i in range(len(lst)):
        min_val = lst[i]
        min_idx = i

        for j in range(i+1, len(lst)):
            if min_val <= lst[j]:
                continue

            min_val = lst[j]
            min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]
            

def main():
    count = random.randint(2, 20)
    arr = []

    for i in range(count):
        arr.append(random.randint(0, 100))

    print("Original list.....", end=': ')
    print(*arr, sep=', ')

    select_sort(arr)

    print("Sorted list.....", end=": ")
    print(*arr, sep=', ')


if __name__ == "__main__":
    main()
