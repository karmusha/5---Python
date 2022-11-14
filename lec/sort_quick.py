# --- Quick sort ---
 
import random
from random import randint
from random import choice


# def quicksort(nums):
#    if len(nums) <= 1:
#        return nums
#    else:
#        q = random.choice(nums)
#        s_nums = []
#        m_nums = []
#        e_nums = []
#        for n in nums:
#            if n < q:
#                s_nums.append(n)
#            elif n > q:
#                m_nums.append(n)
#            else:
#                e_nums.append(n)
#        return quicksort(s_nums) + e_nums + quicksort(m_nums)

# def quicksort(nums, fst, lst):
#    if fst >= lst: return
 
#    i, j = fst, lst
#    pivot = nums[random.randint(fst, lst)]
 
#    while i <= j:
#        while nums[i] < pivot: i += 1
#        while nums[j] > pivot: j -= 1
#        if i <= j:
#            nums[i], nums[j] = nums[j], nums[i]
#            i, j = i + 1, j - 1
#    quicksort(nums, fst, j)
#    quicksort(nums, i, lst)

def quicksort(nums):
    
    if len(nums) <= 1:
       return nums
    else:
       q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
 
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

a = []
for i in range(10):
    a.append(randint(1, 99))
print(a)

a = quicksort(a)
print(a)