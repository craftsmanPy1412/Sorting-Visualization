import matplotlib.pyplot as plt
import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_bars(arr)
            time.sleep(0.2)

def draw_bars(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title("Bubble Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.01)

# Main
if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(20)]
    plt.ion()
    draw_bars(arr)
    bubble_sort(arr)
    plt.ioff()
    plt.show()
