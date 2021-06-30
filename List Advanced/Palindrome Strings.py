text = input().split()

searched_palindrom = input()

palindroms = [n for n in text if n == n[::-1]]

print(palindroms)
print((f"Found palindrome {palindroms.count(searched_palindrom)} times"))
