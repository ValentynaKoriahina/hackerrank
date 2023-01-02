from collections import deque

N = int(input())
d = deque()

def witn_arg(to_do, value):
    global d

    if to_do == 'append':
        d.append(value)
        return d
    elif to_do == 'appendleft':
        d.appendleft(value)
        return d

def no_arg(to_do):
    global d

    if to_do == 'pop':
        d.pop()
        return d
    elif to_do == 'popleft':
        d.popleft()
        return d


for _ in range(N):
    to_do = input()
    if len(to_do.split()) > 1:
        to_do, value = to_do.split()
        witn_arg(to_do, value)
    else:
        no_arg(to_do)

print(*d)
