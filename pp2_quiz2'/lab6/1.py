n = int(input())
nums = map(int, input().split())
squares = map(lambda x: x*x, nums)
print(sum(squares))