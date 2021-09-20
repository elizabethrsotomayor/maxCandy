class Solution:
    def maxCandy(self, height, n):
        start = 0
        end = n-1
        max_area = 0
        while start < end:
            area = min(height[start], height[end])*(end-start-1)

            max_area = max(area, max_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

if __name__ == '__main__':
    t = int(input("Value for number of tests: "))
    for _ in range(t):
        n = int(input("Value for n: "))
        arr = list(map(int, input("Arr values: ").strip().split()))
        obj = Solution()
        print(obj.maxCandy(arr, n))
