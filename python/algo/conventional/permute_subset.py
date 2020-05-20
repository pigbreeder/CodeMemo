#encoding=utf8
#全排列/子集
# 字符串的字典序排第n的字符串是什么
# https://blog.csdn.net/L123012013048/article/details/49538237
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

def previousPermute(nums):
    # 从后往前找第一个下降的数
    for i in range(len(nums) - 1, -1, -1):
        for j in range(len(nums)-1, i+1, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = reversed(nums[i+1:])
                return
    return nums.reverse()
def nextPermute(nums):
    # 从后往前找第一个下降的数
    for i in range(len(nums)-2, -1, -1):
        if nums[i+1] > nums[i]:
            # (end,i)找第一个比nums[i]大的数
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
            #print i,j,nums
            nums[i+1:] = reversed(nums[i+1:])
            return
    return nums.reverse()

def kthPermute(nums, kth):
    ans = []
    t = 1
    multiplier = []
    for i in range(1, nums):
        t *= i
        multiplier.insert(0, t)
    if kth==0 or t*nums < kth:
        return []
    #print multiplier
    num = range(1, nums+1)
    for i in multiplier:
        h = kth // i
        kth = kth % i
        if h == 0:
            continue
        ans.append(num.pop(h-1))
    #print ans,num,ans + num
    return ans + num

def permuteNo(nums=[6,8,4,7,3,2]):
    k = 0
    ans = 0
    flag = {}
    t = 1
    multiplier = [1]
    for i in range(1, len(nums)):
        t *= i
        multiplier.insert(0, t)
    print multiplier
    for i in range(len(nums)):
        tmp = 0
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                tmp += 1
        flag[nums[i]] = 1
       
        ans += multiplier[i] * tmp
        #print i,nums[i],tmp,ans
    return ans + 1
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
print '###################################'
arr = [1,2,7,4,3,1]
print 'original=', arr
previousPermute(arr)
print 'previousPermute=', arr
arr = [1,2,7,4,3,1]
nextPermute(arr)
print 'nextPermute=', arr
print 'kthPermute=',kthPermute(5,13)
print(permuteNo())
