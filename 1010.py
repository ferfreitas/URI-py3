cod,n_pecas,v_uni = input().split(" ")
cod2,n_pecas2,v_uni2 = input().split(" ")

cod = int(cod)
n_pecas = int(n_pecas)
v_uni = float(v_uni)

cod2 = int(cod2)
n_pecas2 = int(n_pecas2)
v_uni2 = float(v_uni2)

total = (n_pecas * v_uni) + (n_pecas2 * v_uni2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
