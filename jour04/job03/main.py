def recursive(x,n):
    if n == 0:
        return 1
    else:
        return x * recursive(x , n - 1)

x = int(input('De quel nombre voulez vous calculer la puissance: '))
n = int(input('Avec quel factoriel: '))

print(x, "puissance de", n, "est égal à :", recursive(x, n))
