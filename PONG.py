import pygame
import tkinter as tk
from tkinter import messagebox

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Pong')

# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)

# Paramètres des raquettes
largeur_raquette = 10
hauteur_raquette = 100
vitesse_raquette = 10

# Paramètres de la balle
taille_balle = 20

# Création des objets
raquette1 = pygame.Rect(30, hauteur_fenetre // 2 - hauteur_raquette // 2, largeur_raquette, hauteur_raquette)
raquette2 = pygame.Rect(largeur_fenetre - 30 - largeur_raquette, hauteur_fenetre // 2 - hauteur_raquette // 2, largeur_raquette, hauteur_raquette)
balle = pygame.Rect(largeur_fenetre // 2 - taille_balle // 2, hauteur_fenetre // 2 - taille_balle // 2, taille_balle, taille_balle)

# Initialisation des variables du jeu
vitesse_balle_x = 5
vitesse_balle_y = 5

# Fonction pour afficher le score
def afficher_score(score1, score2):
    police = pygame.font.SysFont(None, 55)
    texte_score = police.render(f"{score1} - {score2}", True, blanc)
    fenetre.blit(texte_score, [largeur_fenetre // 2 - texte_score.get_width() // 2, 20])

# Boucle principale du jeu
def boucle_jeu():
    global vitesse_balle_x, vitesse_balle_y  # Déclaration des variables globales
    horloge = pygame.time.Clock()
    score1 = 0
    score2 = 0
    vitesse_raquette1 = 0
    vitesse_raquette2 = 0

    en_cours = True
    while en_cours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_w:
                    vitesse_raquette1 = -vitesse_raquette
                if evenement.key == pygame.K_s:
                    vitesse_raquette1 = vitesse_raquette
                if evenement.key == pygame.K_UP:
                    vitesse_raquette2 = -vitesse_raquette
                if evenement.key == pygame.K_DOWN:
                    vitesse_raquette2 = vitesse_raquette
            if evenement.type == pygame.KEYUP:
                if evenement.key == pygame.K_w or evenement.key == pygame.K_s:
                    vitesse_raquette1 = 0
                if evenement.key == pygame.K_UP or evenement.key == pygame.K_DOWN:
                    vitesse_raquette2 = 0

        # Déplacement des raquettes
        raquette1.y += vitesse_raquette1
        raquette2.y += vitesse_raquette2
        # Limiter le mouvement des raquettes
        if raquette1.top < 0:
            raquette1.top = 0
        if raquette1.bottom > hauteur_fenetre:
            raquette1.bottom = hauteur_fenetre
        if raquette2.top < 0:
            raquette2.top = 0
        if raquette2.bottom > hauteur_fenetre:
            raquette2.bottom = hauteur_fenetre

        # Déplacement de la balle
        balle.x += vitesse_balle_x
        balle.y += vitesse_balle_y

        # Collision de la balle avec les murs
        if balle.top <= 0 or balle.bottom >= hauteur_fenetre:
            vitesse_balle_y = -vitesse_balle_y
        # Collision de la balle avec les raquettes
        if balle.colliderect(raquette1) or balle.colliderect(raquette2):
            vitesse_balle_x = -vitesse_balle_x

        # Marquage des points
        if balle.left <= 0:
            score2 += 1
            balle.x = largeur_fenetre // 2 - taille_balle // 2
            vitesse_balle_x = -vitesse_balle_x
        if balle.right >= largeur_fenetre:
            score1 += 1
            balle.x = largeur_fenetre // 2 - taille_balle // 2
            vitesse_balle_x = -vitesse_balle_x

        # Dessiner les objets
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, blanc, raquette1)
        pygame.draw.rect(fenetre, blanc, raquette2)
        pygame.draw.ellipse(fenetre, blanc, balle)
        afficher_score(score1, score2)
        pygame.display.flip()

        # Contrôler la vitesse de la boucle du jeu
        horloge.tick(60)

    pygame.quit()

# Menu de démarrage Tkinter
def menu_demarrage():
    racine = tk.Tk()
    racine.title("Jeu de Pong")

    def commencer_jeu():
        racine.destroy()
        boucle_jeu()

    tk.Label(racine, text="Bienvenue dans Pong", font=("Helvetica", 24)).pack(pady=20)
    tk.Button(racine, text="Commencer le Jeu", command=commencer_jeu, font=("Helvetica", 18)).pack(pady=10)
    tk.Button(racine, text="Quitter", command=racine.quit, font=("Helvetica", 18)).pack(pady=10)

    racine.mainloop()

# Lancer le menu de démarrage
menu_demarrage()
