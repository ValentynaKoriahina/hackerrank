from collections import OrderedDict

N = int(input())
bought_items = OrderedDict()

for _ in range(N):
    item = input()
    item_name, sep, net_price = item.rpartition(' ')
    if item_name not in bought_items:
        bought_items[item_name] = int(net_price)
    else:
        bought_items[item_name] += int(net_price)

for item_name, net_price in bought_items.items():
    print(item_name, net_price)

