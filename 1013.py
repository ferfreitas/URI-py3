A,B,C = map(int, input().split())

maior1 = (A + B + abs(A-B)) / 2

maior2 = (maior1 + C + abs(maior1 - C)) / 2

print("%d eh o maior" %maior2)
