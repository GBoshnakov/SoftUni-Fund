number = input()
import heapq

list1 = list(number)

largest_number = (heapq.nlargest(len(number), list1))

largest_number = "".join(largest_number)

print(largest_number)