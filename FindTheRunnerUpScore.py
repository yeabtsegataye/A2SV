if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    nums = sorted(arr)
for i in range(n):
    if nums[i]<nums[n-1]:
        b = nums[i]
print(b)
