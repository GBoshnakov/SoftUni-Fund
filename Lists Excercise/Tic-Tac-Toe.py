def check_if_winner(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return 1
    elif a == 2 and b == 2 and c == 2:
        return 2
    else:
        return 0

def who_the_winner_is(result):
    if result == 1:
        print("First player won")
    elif result == 2:
        print("Second player won")

first_line = [int(n) for n in input().split()]
second_line = [int(n) for n in input().split()]
third_line = [int(n) for n in input().split()]


result = check_if_winner(first_line[0], first_line[1], first_line[2])
if result == 1 or result == 2:
    who_the_winner_is(result)
else:
    result = check_if_winner(second_line[0], second_line[1], second_line[2])
    if result == 1 or result == 2:
        who_the_winner_is(result)
    else:
        result = check_if_winner(third_line[0], third_line[1], third_line[2])
        if result == 1 or result == 2:
            who_the_winner_is(result)
        else:
            result = check_if_winner(first_line[0], second_line[0], third_line[0])
            if result == 1 or result == 2:
                who_the_winner_is(result)
            else:
                result = check_if_winner(first_line[1], second_line[1], third_line[1])
                if result == 1 or result == 2:
                    who_the_winner_is(result)
                else:
                    result = check_if_winner(first_line[2], second_line[2], third_line[2])
                    if result == 1 or result == 2:
                        who_the_winner_is(result)
                    else:
                        result = check_if_winner(first_line[0], second_line[1], third_line[2])
                        if result == 1 or result == 2:
                            who_the_winner_is(result)
                        else:
                            result = check_if_winner(first_line[2], second_line[1], third_line[0])
                            if result == 1 or result == 2:
                                who_the_winner_is(result)
                            else:
                                print("Draw!")