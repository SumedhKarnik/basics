#!/usr/bin/python3
import random


def insert_asc(data, n):
    if n <= 1:
        return

    insert_asc(data, n-1)

    nth = data[n-1]
    j = n - 2
    while (j >= 0) and (data[j] > nth):
        data[j+1] = data[j]
        j = j - 1
   
    data[j+1] = nth


def insert_desc(data):
    if len(data) <= 1:
        return data

    for i in range(1, len(data)):
        ith = data[i]
        j = i - 1

        while (j>=0) and (data[j] < ith):
            data[j+1] = data[j]
            j = j - 1

        data[j+1] = ith
    
              
def main():
    sz = random.randint(2, 20)

    lst = []
    for i in range(sz):
        lst.append(random.randint(0, 100))
    
    print("Original....", end=": ")
    print(*lst, sep=', ')

    insert_asc(lst, len(lst))
    print("Ascending....", end=": ")
    print(*lst, sep=', ')

    insert_desc(lst)
    print("Descending...", end=": ")
    print(*lst, sep=', ') 


if __name__ == "__main__":
    main()
