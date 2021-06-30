# def find_palindromes(string_as_list):
#
#
#     for number in string_as_list:
#         is_Palindrome = True
#         if len(number) % 2 == 0:
#             half = int(len(number) / 2)
#             left_half = number[0:half]
#             right_half = "".join(reversed(number[half:]))
#             for i in range(len(left_half)):
#                 if left_half[i] == right_half[i]:
#                     continue
#                 else:
#                     is_Palindrome = False
#                     print(False)
#                     break
#             if is_Palindrome:
#                 print(True)
#         else:
#             half = int(len(number) / 2)
#             left_half = number[0:half]
#             right_half = "".join(reversed(number[half + 1:]))
#             for i in range(len(left_half)):
#                 if left_half[i] == right_half[i]:
#                     continue
#                 else:
#                     is_Palindrome = False
#                     print(False)
#                     break
#             if is_Palindrome:
#                 print(True)
#
# numbers = input().split(", ")
#
# find_palindromes(numbers)

def find_palindromes(string_as_list):
    for number in string_as_list:
        reversed_number = "".join(reversed(number))
        if number == reversed_number:
            print(True)
        else:
            print(False)

numbers = input().split(", ")

find_palindromes(numbers)


