"""
Given an array, find the index of the first local maximum (peak) found.
Collection of routines to perform the task.
"""


def find_peak_walking(arr):
    """
    The basic algorithm will walk the array.
        Args:
            arr: list of numbers or Numpy 1D array
        Returns:
            index of the first local max found
    """

    n = len(arr)

    for i in range(0, n):

        prev = arr[i] if i == 0 else arr[i - 1]
        succ = arr[i] if i == n - 1 else arr[i + 1]

        if arr[i] >= prev and arr[i] >= succ:
            return i


def find_peak_binary_search(arr):
    """
    The better algorithm will recursively analyse half the array.
        Args:
            arr: list of numbers or Numpy 1D array
        Returns:
            index of the first local max found
    """
    n, half_len = len(arr), int(len(arr) / 2)

    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] if arr[0] >= arr[1] else arr[1]

    if arr[half_len] < arr[half_len - 1]:
        return find_peak_binary_search(arr[:half_len])
    elif arr[half_len] < arr[half_len + 1]:
        return find_peak_binary_search(arr[half_len + 1 :])
    else:
        return arr[half_len]
