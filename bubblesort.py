#!/usr/bin/env python3
import os

# Bubble Sort algorythm implementation
# with 2 enhancements:
# 1. Do not try sorted part during next traversal
# 2. Exit if array is already sorted

# Idea 1: compare bubble up and bubble down traversals
# Idea 1.1: print number of swaps for bubble up/bubble down
# Idea 1.2: arbitrary turn on or off each of bubblesort enhancements
# Idea 2: move swap into separate function


x=input("List of numbers comma separated:\n");
a=[int(i) for i in x.split(',')]
#a=[6,4,7,1,4,2]
total_swaps=1
swapped=1

print(a)
for k in range(1,len(a)):
    if swapped != 0:
        swapped=0
        for i in range(0,len(a)-k):
            if a[i] > a[i+1]:
                tmp=a[i+1]
                a[i+1]=a[i]
                a[i]=tmp
                total_swaps+=1
                swapped+=1

print(a,total_swaps)


