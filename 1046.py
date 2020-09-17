a,b=map(int, input().split())

if a>b:
    y=24-a
    h=y+b
    print("O JOGO DUROU %d HORA(S)" %h)
elif b>a:
    h=b-a
    print("O JOGO DUROU %d HORA(S)" %h)
elif a==b:
    h=24
    print("O JOGO DUROU %d HORA(S)" %h)
