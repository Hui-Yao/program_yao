'''
题目：
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例：
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

分析：只要相邻两元素不同，则将后面一个元素赋值到列表前端。
需要判定相邻两元素是否相同，所以要维护一个左指针，那么右指针为左指针+1。还需要维护一个变量表示换到前面去的最后一个无重复元素的索引。

'''

def remove(nums):
    j = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[j] = nums[i+1]
            j += 1
    return j

print(remove([0,0,1,1,1,2,2,3,3,4]))