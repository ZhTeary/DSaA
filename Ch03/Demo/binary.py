# 递归 二分查找

def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)>>1
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
            return binary_search(data,target,low,high)
        else:
            low = mid + 1
            return binary_search(data,target,low,high)