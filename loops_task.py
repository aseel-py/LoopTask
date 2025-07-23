# Part 1: For Loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Part 1 - Numbers:")
for num in numbers:
    print(num)

print("\nPart 1 - Squares:")
for num in numbers:
    print(num ** 2)


# Part 2: While Loop

nums = [3, 6, 9, 12, 15]

print("\nPart 2 - Numbers until > 10:")
i = 0
while i < len(nums) and nums[i] <= 10:
    print(nums[i])
    i += 1

print("\nPart 2 - Sum until > 20:")
i = 0
total = 0
while i < len(nums) and total <= 20:
    total += nums[i]
    print("Current sum:", total)
    i += 1


# Part 3: Challenge

rand_nums = [5, 10, 15, 20, 25, 30]

count = 0
for num in rand_nums:
    if num % 5 == 0:
        count += 1

print("\nPart 3 - Count divisible by 5:", count)
