
def binary_search_left_most(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            if nums[mid] == target: ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

def binary_search_rec(nums, target, left, right):
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search_rec(nums, target, left, mid - 1)
        else:
            return binary_search_rec(nums, target, mid + 1, right)

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