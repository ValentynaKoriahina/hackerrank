from collections import Counter


def mySolution():
    X = int(input())
    all_shoe_sizes = Counter(map(int, input().split()))
    number_of_customers = int(input())
    money_earned = 0

    for i in range(number_of_customers):
        shoe_size, price = map(int, input().split())
        all_shoe_sizes[shoe_size] -= 1
        if all_shoe_sizes[shoe_size] >= 0:
            money_earned += price
        else:
            pass

    print(money_earned)


mySolution()