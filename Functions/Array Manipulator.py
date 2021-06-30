def exchange(array, given_index):
    array = array[given_index + 1:] + array[:given_index + 1]


array = input().split()

command = input().split()

while "end" not in command:
    pass