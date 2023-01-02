import collections

N = int(input())

words = collections.OrderedDict()

for _ in range(N):
    text = input()
    if text not in words:
        words[text] = 1
    else:
        words[text] += 1

print(len(words))
print(*words.values())

# SOLUTION 2 - collections.Counter()

N = int(input())
text = []
for _ in range(N):
    text.append(input())

text = collections.Counter(text).items()

print(len(text))
for i in text:
    print(i[1], end=' ')