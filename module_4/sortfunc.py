import math, time

def bubble_sort(ls):
    start = time.time()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if (ls[i] > ls[i+1]):
                ls[i],ls[i+1] = ls[i+1],ls[i]
                swapped = True
    stop = time.time()
    time_used = stop - start
    return ls,time_used

def selection_sort(ls):
    start = time.time()
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    stop = time.time()
    time_used = stop - start
    return ls,time_used

def insertion_sort(ls):
    start = time.time()
    for i in range (1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = key
    stop = time.time()
    time_used = stop - start
    return ls,time_used
