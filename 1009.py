nome = input()
sal_fixo = float(input())
vendas = float(input())

sal_total = sal_fixo + (vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(sal_total))
