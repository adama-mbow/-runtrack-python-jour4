def multiple(): # on défini une fonction appelé multiple
    L = [8, 24,48,2,16] # créer une liste L
    L3 = [] # créer une liste vide appelé L3
    for i in L: # parcourir la liste L
        if i % 3 == 0: # on pause la condition si l'élément i de la liste L est multiple de 3
            L3.append(i) #ajouter la multiple de 3 de la liste L sur la la liste vide L3
    print(L3) # afficher les éléments de la liste L3 qui sont des muiltiples de 3
    print(len(L3)) # afficher le nombre d'élément de la liste L3
multiple()
