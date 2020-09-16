N = int(input())

a = int(N / 365)

m = int((N % 365) / 30)

d = int((N - (a * 365) - (m * 30)))

print("{} ano(s)".format(a))
print("{} mes(es)".format(m))
print("{} dia(s)".format(d))
