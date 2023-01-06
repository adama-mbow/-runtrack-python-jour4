def produit():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    L2 = []
    mult = 1
    for i in L:
        if i >= 25 and i <= 90:
            L2.append(i)
            mult *= i
    print(L2)
    print(mult)

        
produit()