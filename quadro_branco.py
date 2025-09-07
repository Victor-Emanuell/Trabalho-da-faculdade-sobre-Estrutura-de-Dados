lista = [835.83, 25.19, 894.65, 263.66, 752.41]

def quick(arr):
    def quicksort (arr, left, right):
        if left < right: 
            pi = partition(arr, left, right)
            quicksort(arr, left, pi-1)
            quicksort(arr, pi +1, right)

    def partition(arr, left, right):
        pivot = arr[right]

        i = left - 1

        for j in range(left, right):
            if arr[j] <= pivot:
                i = i + 1 
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i+1

    quicksort(arr, 0, len(arr) - 1)


quick(lista)
print(lista)