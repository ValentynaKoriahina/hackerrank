from collections import namedtuple

N = int(input())
student = namedtuple('student',input().strip().split())
sumMarks = 0

for _ in range(N):
    values = input().strip().split()
    instance = student(*values)
    sumMarks += int(instance.MARKS)

avgMarks = sumMarks / N

print('%.2f' % avgMarks)
