#!/usr/bin/python3
import random


def quick_asc(lst):
    if len(lst) <= 1:
        return lst

    pivot = random.randint(0, len(lst)-1)
    pivot = lumoto(lst, pivot)
 
    left = lst[:pivot]
    right = lst[pivot+1:]

    quick_asc(left)
    quick_asc(right)

    tmp = lst[pivot]
    lst.clear()

    if left:
        lst.extend(left)
    lst.append(tmp)
    if right:
        lst.extend(right)


def lumoto(dt, pivot):
    if len(dt) <= 1:
        return pivot

    dt[0], dt[pivot] = dt[pivot], dt[0]
    left = right = 0

    while right < len(dt)-1:
        right = right + 1
        if dt[right] <= dt[0]:
            left = left + 1
            dt[left], dt[right] = dt[right], dt[left]
    
    dt[left], dt[0] = dt[0], dt[left]
    return left


def quick_desc(lst):
    if len(lst) <= 1:
        return

    pivot = random.randint(0, len(lst)-1)
    pivot = hoares(lst, pivot)

    left = lst[:pivot]
    right = lst[pivot+1:]

    quick_desc(left)
    quick_desc(right)

    tmp = lst[pivot]
    lst.clear()

    if left:
        lst.extend(left)
    lst.append(tmp)
    if right:
        lst.extend(right)


def hoares(dt, pivot):
    if len(dt) <= 1:
        return pivot

    dt[0], dt[pivot] = dt[pivot], dt[0]

    left = 1
    right = len(dt)

    while (left < right) and (left<len(dt)):
        if dt[left] < dt[0]:
            right = right - 1
        else:
            left = left + 1

        if right == len(dt):
            continue

        if (dt[left] < dt[0]) and (dt[right] >= dt[0]):
            dt[left], dt[right] = dt[right], dt[left]

    right = right - 1 
    dt[0], dt[right] = dt[right], dt[0]

    return right

 
def main():
    sz = random.randint(2, 20)
    data = []

    for i in range(sz):
        data.append(random.randint(0, 100))

    print("Original ....", end=": ")
    print(*data, sep=", ")

    quick_asc(data)

    print("Sorted....", end=": ")
    print(*data, sep=", ")

    quick_desc(data)
    
    print("Descending....", end=": ")
    print(*data, sep=", ")


if __name__ == "__main__":
    main()
