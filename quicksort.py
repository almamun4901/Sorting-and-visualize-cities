# Name: Md Al Mamun
#Date: 11/09/2022
#Purpose: Lab3

# This part is actually functions for doing the sorting

from city import City


def compare_population_ints(a, b):
    return a.population <= b.population


def compare_latitude(a, b):
    return a.latitude <= b.latitude


def compare_strings(a, b):
    return a.city_name.lower() <= b.city_name.lower()

def partition(the_list, p, r, compare_func):

    pivot = the_list[r]

    i = p - 1

    for j in range(p, r):
        if compare_func(the_list[j], pivot):
            i = i + 1

            (the_list[i], the_list[j]) = (the_list[j], the_list[i])

    (the_list[i + 1], the_list[r]) = (the_list[r], the_list[i + 1])
    return i + 1

def quicksort(the_list, compare_func, p=None, r=None):
    if p == None and r == None:
        p = 0
        r = len(the_list) - 1

    if p < r:
        pivot = partition(the_list, p, r,compare_func)

        quicksort(the_list, compare_func, p, pivot - 1)
        quicksort(the_list, compare_func, pivot + 1, r)


def sort(the_list, compare_func):
    return quicksort(the_list, compare_func)