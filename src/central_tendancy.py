def mean(*nums):
    if type(nums[0]) == list or type(nums[0]) == tuple:
        nums = nums[0]
    summed_nums = 0
    count = 0
    for n in nums:
        summed_nums += n
        count += 1
    return summed_nums / count

def median(*nums):
    if type(nums[0]) == list or type(nums[0]) == tuple:
        nums = nums[0]
    nums = sorted(nums)
    no_of_elems = len(nums)
    if no_of_elems % 2 != 0:
        return nums[no_of_elems // 2]
    else:
        return 0.5 * (nums[no_of_elems//2 - 1] + nums[no_of_elems // 2])

if __name__ == "__main__":
    print(median(1,2,3))
    print(median(1,2,3,4))
