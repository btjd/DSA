def trapRainWater(heights):
    # https://discuss.leetcode.com/topic/51926/o-n-time-o-1-space-python-just-for-fun
    left = 0
    right = len(heights) - 1
    ans = 0
    while left < right:
        if heights[left] >= heights[right]:
            ans += max(0, heights[right] - heights[right - 1])
            heights[right - 1] = max(heights[right], heights[right - 1])
            right -= 1
        else:
            ans += max(0, heights[left] - heights[left + 1])
            heights[left + 1] = max(heights[left], heights[left + 1])
            left += 1
    return ans

alist = [0,1,0,2,1,0,1,3,2,1,2,1]
# alist = [2, 0, 2]
print trapRainWater(alist)