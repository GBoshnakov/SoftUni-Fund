string_as_list = input().split()



# result = []
#
# for index in range(len(string_as_list)):
#     if int(string_as_list[index]) > 0:
#         result.append(int(string_as_list[index]) - 2 * int(string_as_list[index]))
#     else:
#         result.append(abs(int(string_as_list[index])))
#
#
string_as_list = [-1 * int(n) for n in string_as_list]
print(string_as_list)
