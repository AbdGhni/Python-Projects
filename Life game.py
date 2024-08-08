from tkinter import *
from random import randint

# Fonction pour créer une grille initiale
def liste():
    return [[0 for _ in range(60)] for _ in range(60)]

# Fonction pour activer une cellule
def ini(x, y):
    l[x][y] = 1
    ca.delete(r[x][y])
    r[x][y] = ca.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill='black')

# Fonction pour détruire une cellule
def détruit(x, y):
    l[x][y] = 0
    ca.delete(r[x][y])
    r[x][y] = ca.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill='white')

# Fonction pour générer aléatoirement un nombre de cellules vivantes
def aléatoire(nombre):
    n = 0
    while n != nombre:
        x = randint(0, 59)
        y = randint(0, 59)
        ini(x, y)
        n += 1

# Fonction pour démarrer l'animation
def go():
    global m
    if m == 1:
        comptage()
        f.after(500, go)

# Fonction pour arrêter l'animation
def stop():
    global m
    m = 0

# Fonction pour continuer l'animation
def continuer():
    global m
    m = 1
    go()

# Fonction pour ajouter une cellule lorsque l'utilisateur clique
def rajouter(event):
    x = event.x // 10
    y = event.y // 10
    ini(x, y)

# Fonction pour compter les voisins
def comptage():
    global m
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i == 0 and j == 0:  # Coin en haut à gauche
                compt = l[0][1] + l[1][0] + l[1][1]
            elif i == 0 and j == 59:  # Coin en haut à droite
                compt = l[0][58] + l[1][58] + l[1][59]
            elif i == 59 and j == 0:  # Coin en bas à gauche
                compt = l[58][0] + l[58][1] + l[59][1]
            elif i == 59 and j == 59:  # Coin en bas à droite
                compt = l[58][59] + l[58][58] + l[59][58]
            elif 0 < i < 59 and j == 0:  # Bord de gauche
                compt = l[i-1][0] + l[i-1][1] + l[i][1] + l[i+1][1] + l[i+1][0]
            elif 0 < i < 59 and j == 59:  # Bord de droite
                compt = l[i-1][59] + l[i-1][58] + l[i][58] + l[i+1][58] + l[i+1][59]
            elif i == 0 and 0 < j < 59:  # Bord du haut
                compt = l[0][j-1] + l[1][j-1] + l[1][j] + l[1][j+1] + l[0][j+1]
            elif i == 59 and 0 < j < 59:  # Bord du bas
                compt = l[59][j-1] + l[58][j-1] + l[58][j] + l[58][j+1] + l[59][j+1]
            else:  # Toutes les autres cellules
                compt = (l[i-1][j-1] + l[i-1][j] + l[i-1][j+1] +
                         l[i][j+1] + l[i+1][j+1] + l[i+1][j] +
                         l[i+1][j-1] + l[i][j-1])
            c[i][j] = compt
    régle()

# Fonction pour appliquer les règles du jeu de la vie
def régle():
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 0 and c[i][j] == 3:
                ini(i, j)
            elif (l[i][j] == 1 and c[i][j] < 2) or (l[i][j] == 1 and c[i][j] > 3):
                détruit(i, j)

# Programme principal
m = 1
l = liste()
c = liste()
r = liste()

f = Tk()
f.title("Jeu de la Vie de Conway")

ca = Canvas(f, width=600, height=600, background="white")
ca.bind("<Button-1>", rajouter)
ca.pack()

# Ajouter la signature
ca.create_text(10, 590, anchor='sw', text="Codé par Ghani Abdullah", fill="black", font=('Arial', 8))

# Boutons
s = Spinbox(f, values=(100, 200, 300, 400, 500, 600))
s.pack()

bouton1 = Button(f, text="Générer les cellules vivantes aléatoirement", command=lambda: aléatoire(int(s.get())))
bouton1.pack()

bouton2 = Button(f, text="Voir", command=go)
bouton2.pack()

bouton3 = Button(f, text="Pause", command=stop)
bouton3.pack()

bouton4 = Button(f, text="Continuer", command=continuer)
bouton4.pack()

f.mainloop()
