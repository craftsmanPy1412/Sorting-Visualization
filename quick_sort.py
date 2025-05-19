import matplotlib.pyplot as plt
import random
import time

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        draw_bars(arr, low, high, pivot_index)
        time.sleep(0.3)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # pivot
    i = low - 1         # index of smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_bars(arr, low, high, high)
            time.sleep(0.2)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    draw_bars(arr, low, high, i+1)
    time.sleep(0.2)
    return i + 1

def draw_bars(arr, low=0, high=None, pivot=None):
    plt.clf()
    colors = ['skyblue'] * len(arr)
    if high is not None:
        for i in range(low, high + 1):
            colors[i] = 'orange'
    if pivot is not None:
        colors[pivot] = 'red'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title("Quick Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.01)

# Main
if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    plt.ion()
    draw_bars(arr)
    quick_sort(arr, 0, len(arr) - 1)
    plt.ioff()
    plt.show()
