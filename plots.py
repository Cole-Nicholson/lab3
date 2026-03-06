import time
from typing import *
import unittest
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
import functions
from functions import make_range, occurs, has_dup, insertion_sort, LLNode, LinkedList

num_points = 15
trials_per_n = 4

def sample_values(n_max: int) -> list[int]:
    step = (n_max -1)/ (num_points - 1)
    return [round(1 + i * step) for i in range(num_points)]

def make_lists(n: int) -> LinkedList:
    ll = None
    for i in range(n-1, -1, -1):
        ll = LLNode(i, ll)
    return ll

def runtime_make_range(n: int) -> float:
    times : list[float] = []
    for _ in range(trials_per_n):
        start : float = time.perf_counter()
        make_range(n)
        end : float = time.perf_counter()
        times.append(end-start)
    return sum(times) / len(times)

def runtime_occurs(n: int) -> float:
    times : list[float] = []
    target = -1
    ll = make_lists(n)
    for _ in range(trials_per_n):
        start : float = time.perf_counter()
        occurs(ll, target)
        end : float = time.perf_counter()
        times.append(end-start)
    return sum(times) / len(times)

def runtime_has_dup(n: int) -> float:
    times : list[float] = []
    ll = make_lists(n)
    for _ in range(trials_per_n):
        start : float = time.perf_counter()
        has_dup(ll)
        end : float = time.perf_counter()
        times.append(end-start)
    return sum(times) / len(times)

def runtime_insertion_sort(n: int) -> float:
    times: list[float] = []
    ll = make_lists(n)
    for _ in range(trials_per_n):
        start: float = time.perf_counter()
        insertion_sort(ll)
        end: float = time.perf_counter()
        times.append(end-start)
    return sum(times) / len(times)

def make_graph(x_axis: list[float], y_axis: list[float], title: str):
    plt.plot(x_axis, y_axis, marker = 'o')
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.title(title)
    plt.grid(True)
    plt.show()

def graph_function(runtime_function, n_max: int, title: str):
    x_axis = sample_values(n_max)
    y_axis = []
    for n in x_axis:
        y_axis.append(runtime_function(n))
    make_graph(x_axis, y_axis, title)


if (__name__ == '__main__'):

    graph_function(runtime_make_range, 20000, "Worst case of make range")
    graph_function(runtime_occurs, 20000, "Worst case of occurs")
    graph_function(runtime_has_dup, 2000, "Worst case of has_dup")
    graph_function(runtime_insertion_sort, 2000, "Worst case of insertion sort")
    

    
    
    


