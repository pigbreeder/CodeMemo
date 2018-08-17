#encoding=utf8
#全排列/子集
#
#全不同
def permute(nums, st, ed, ret):
    if st == ed:
        ret.append(nums[:])
        return
    for i in range(st, ed):

        nums[i], nums[st] = nums[st], nums[i]
        #print st,ed,i,nums
        permute(nums, st + 1, ed, ret)
        nums[i], nums[st] = nums[st], nums[i]

def permuteUnique(nums, st, ed, ret):
    if st == ed:
        ret.append(nums[:])
        return
    flag = set()
    for i in range(st, ed):
        if nums[i] in flag:
            continue
        flag.add(nums[i])
        nums[i], nums[st] = nums[st], nums[i]
        #print st, i, nums
        permuteUnique(nums, st + 1, ed, ret) # 这里是st + 1
        nums[i], nums[st] = nums[st], nums[i]

def subset(nums, st, ed, tmp, ret):
    if st == ed:
        ret.append(tmp[:])
        return
    subset(nums, st + 1, ed, tmp[:], ret)
    subset(nums, st + 1, ed, tmp[:] + [nums[st]], ret)

# 枚举的是长度
def subset2(nums, st, ed, tmp, ret):
    if st == ed:
        # ret.append(tmp[:])
        return
    
    for i in range(st, ed):
        if i > st and nums[i] == nums[i - 1]:
            continue
        tmp.append(nums[i])
        ret.append(tmp[:])
        subset2(nums, i + 1, ed, tmp ,ret) # 这里是i + 1
        tmp.pop()

arr1 = [1,2,2]
arr2 = [1,2,3]
r = []
permute(arr2, 0, 3, r)
print 'permute=', r
r = []
permuteUnique(arr1, 0, 3, r)
print 'permuteUnique=', r
r = []
subset(arr2, 0, 3, [], r)
print 'subset=', r
r = []
subset2(arr1, 0, 3, [], r)
print 'subset2=', r
