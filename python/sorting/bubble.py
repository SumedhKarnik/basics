#!/usr/bin/python3
import random


def bubble_sort(data):
    
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

def main():
    sz = random.randint(2, 20)

    lst = []
    for i in range(sz):
        lst.append(random.randint(0, 100))

    print("Original....", end=": ")
    print(*lst, sep=', ')

    bubble_sort(lst)

    print("Sorted....", end=": ")
    print(*lst, sep=', ')


if __name__ == "__main__":
    main()
