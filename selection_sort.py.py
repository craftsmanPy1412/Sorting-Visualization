import matplotlib.pyplot as plt
import time
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        draw_bars(arr)
        time.sleep(0.2)
    return arr

def draw_bars(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.title("Selection Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.01)

if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original:", data)
    print("Sorted:", selection_sort(data))
    plt.ioff()
    plt.show()
