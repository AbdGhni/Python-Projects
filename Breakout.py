import pygame
import sys


pygame.init()


largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Casse-briques')


noir = (0, 0, 0)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
bleu = (0, 0, 255)


largeur_raquette = 100
hauteur_raquette = 15
vitesse_raquette = 10


taille_balle = 20
vitesse_balle_x = 4
vitesse_balle_y = -4


def creer_briques(niveau):
    briques = []
    largeur_brique = 75
    hauteur_brique = 30
    espacement_brique = 10
    for i in range(7 + niveau):  
        for j in range(5):
            brique = pygame.Rect(i * (largeur_brique + espacement_brique) + 50, j * (hauteur_brique + espacement_brique) + 50, largeur_brique, hauteur_brique)
            briques.append(brique)
    return briques


def afficher_texte(texte, police, couleur, position, taille=48):
    font = pygame.font.SysFont(police, taille)
    texte_surface = font.render(texte, True, couleur)
    rect = texte_surface.get_rect(center=position)
    fenetre.blit(texte_surface, rect)


def ecran_game_over(score):
    fenetre.fill(noir)
    afficher_texte("GAME OVER", "Helvetica", blanc, (largeur_fenetre // 2, hauteur_fenetre // 2 - 50))
    afficher_texte(f"Score: {score}", "Helvetica", blanc, (largeur_fenetre // 2, hauteur_fenetre // 2 + 10))
    afficher_texte("Appuyez sur R pour recommencer", "Helvetica", blanc, (largeur_fenetre // 2, hauteur_fenetre // 2 + 70))
    pygame.display.flip()


def boucle_jeu(niveau):
    global vitesse_balle_x, vitesse_balle_y
    horloge = pygame.time.Clock()
    score = 0
    raquette = pygame.Rect(largeur_fenetre // 2 - largeur_raquette // 2, hauteur_fenetre - hauteur_raquette - 20, largeur_raquette, hauteur_raquette)
    balle = pygame.Rect(largeur_fenetre // 2 - taille_balle // 2, hauteur_fenetre // 2 - taille_balle // 2, taille_balle, taille_balle)
    briques = creer_briques(niveau)

    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and raquette.left > 0:
            raquette.x -= vitesse_raquette
        if touches[pygame.K_RIGHT] and raquette.right < largeur_fenetre:
            raquette.x += vitesse_raquette

        balle.x += vitesse_balle_x
        balle.y += vitesse_balle_y

        if balle.left <= 0 or balle.right >= largeur_fenetre:
            vitesse_balle_x = -vitesse_balle_x
        if balle.top <= 0:
            vitesse_balle_y = -vitesse_balle_y
        if balle.bottom >= hauteur_fenetre:
            ecran_game_over(score)
            while True:
                for evenement in pygame.event.get():
                    if evenement.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_r:
                        return boucle_jeu(niveau)  

        if balle.colliderect(raquette):
            vitesse_balle_y = -vitesse_balle_y

        briques_a_supprimer = []
        for brique in briques:
            if balle.colliderect(brique):
                vitesse_balle_y = -vitesse_balle_y
                briques_a_supprimer.append(brique)
                score += 1

        for brique in briques_a_supprimer:
            briques.remove(brique)

        if not briques:
            niveau += 1
            briques = creer_briques(niveau)
            balle.x = largeur_fenetre // 2 - taille_balle // 2
            balle.y = hauteur_fenetre // 2 - taille_balle // 2
            vitesse_balle_x = 4
            vitesse_balle_y = -4

        fenetre.fill(noir)
        pygame.draw.rect(fenetre, blanc, raquette)
        pygame.draw.ellipse(fenetre, rouge, balle)
        for brique in briques:
            pygame.draw.rect(fenetre, bleu, brique)

        afficher_texte(f"Score: {score}", "Helvetica", blanc, (10, 10))

        
        afficher_texte("Jeu codé par Ghani Abdullah", "Helvetica", blanc, (130, hauteur_fenetre - 20), taille=20)

        pygame.display.flip()
        horloge.tick(60)


niveau_initial = 1
boucle_jeu(niveau_initial)
