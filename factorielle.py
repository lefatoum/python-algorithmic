fact = int(input("Choisir un nombre entier: \n"))
res = 1
for i in range(2, fact+1):
    res = res * i
print(res)