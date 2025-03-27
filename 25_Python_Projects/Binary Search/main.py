from termcolor import colored
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(colored(f"Target {target} found at index {mid}!", "magenta"))
            return mid
        elif arr[mid] > target:
            print(colored(f"Target {target} is smaller than {arr[mid]}, searching left half...", "yellow"))
            right = mid - 1
        else:
            print(colored(f"Target {target} is larger than {arr[mid]}, searching right half...", "cyan"))
            left = mid + 1
    print(colored(f"Target {target} not found in the array!", "red"))
    return -1
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    target = 13
    binary_search(arr, target)
