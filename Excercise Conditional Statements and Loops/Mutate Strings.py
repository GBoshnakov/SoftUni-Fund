word1 = input()
word2 = input()

result = ""

previous_str = word1

for index in range (len(word1)):
    for i in range (index+1):
        result += word2[i]
    for i in range(index+1, len(word1)):
        result += word1[i]
    if result == previous_str:
        result = ""
        continue
    else:
        print(result)
        previous_str = result
        result = ""