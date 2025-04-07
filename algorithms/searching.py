
def binary_search_left_most(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    ans = -1

    


def binary_search(nums, target):
    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    print("Target is at index:", binary_search([1,3,5,7,9,15,20], 3))