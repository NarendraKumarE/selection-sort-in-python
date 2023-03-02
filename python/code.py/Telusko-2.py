def sort (nums):
    for i in range (7):
        minpos = i
        for j in range (i,8):
            if nums[j] < nums[minpos]:
                minpos = j

        tem = nums [i]
        nums[i] = nums [minpos]
        nums[minpos] = tem
        print(nums)
nums = [5,3,8,6,9,11,7,2]
sort(nums)
print(nums)