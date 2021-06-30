numbers = input().split(", ")

nums = [int(num) for num in numbers ]





even_numbers_indexes = [index for index in range(len(nums)) if nums[index] % 2 == 0]

#even_numbers_indexes = list(filter(lambda el: el % 2 == 0, nums))

#even_numbers_indexes = [nums.index(el) for el in list(filter(lambda el: el % 2 == 0, nums))]

print(even_numbers_indexes)