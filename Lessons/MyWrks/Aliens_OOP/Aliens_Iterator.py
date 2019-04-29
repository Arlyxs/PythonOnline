nums = [7, 8, 9, 5]


for i in nums:
    print(i)

print('=======')

it = iter(nums)
print(it.__next__())
print(it.__next__())

print('=======')
