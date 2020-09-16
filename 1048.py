sal = float(input())

if sal > 0 and sal <= 400.00:
    reajuste = sal * 0.15
    novo = sal + reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 15 %")
elif sal > 400.00 and sal <= 800.00:
    reajuste = sal * 0.12
    novo = sal + reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 12 %")
elif sal > 800.00 and sal <= 1200.00:
    reajuste = sal * 0.10
    novo = sal + reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 10 %")
elif sal > 1200.00 and sal <= 2000.00:
    reajuste = sal * 0.07
    novo = sal + reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 7 %")
else:
    reajuste = sal * 0.04
    novo = sal + reajuste
    print("Novo salario: {:.2f}".format(novo))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 4 %")
