    #Binary Search
    # Time Complexity   - O(logn)
    # Space Complexity  - O(1)

#descending Order

def search(nums,target):
        start = 0
        end = len(nums) - 1
        while end >= start:
            middle = (start + end) // 2
            #print('Start : ', start, 'End : ', end, 'Mid : ', middle)
            if nums[middle] == target:
                # its for repeating numbers
                if nums[middle] == nums[middle-1]:
                     end = middle -1
                else:      
                    return middle
            elif nums[middle] > target:
                start = middle + 1
            elif nums[middle] < target:
                end = middle - 1
        return -1

print(search([7,6,5,4,2,1],7))
print(search([6,5,4,2,1],1))
print(search([8,8,8,8,6,6,6,6,5,5,4,4],4))
print(search([4,3,2,1],5))
print(search([],1))