x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())
if (x2 <= x1 <= x2 + w2 or x1 <= x2 <= x1 + w1) and (y2 <= y1 <= y2 + w2 or y1 <= y2 <= y1 + w1):
    print('YES')
else:
    print('NO')