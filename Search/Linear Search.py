    #Linear Search
    # Time Complexity   - O(n)
    # Space Complexity  - O(1)


def search(nums, target):
    pos = 0
    while pos < len(nums):
        if nums[pos] == target:
            return pos
        pos += 1
    return -1

print(search([4,5,2,3,7,9],3))
print(search([],4))
print(search([1,2,4,3,],5))
print(search([6,9,2,4,],6))