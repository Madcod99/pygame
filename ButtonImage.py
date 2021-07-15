import pygame

from Button import Button


class ButtonImage(Button):
    def __init__(self,  message, taille, position, couleur, couleur_click, image, action=None):
        Button.__init__(self,  message, taille, position, couleur, couleur_click, action=None)
        self.image = image


    def afficher(self, surface):
        mouse_taille = pygame.mouse.get_pos()

        if (self.position[0] < mouse_taille[0] < self.position[0] + self.taille[0]) and (
                self.position[1] < mouse_taille[1] < self.position[1] + self.taille[1]):

            # click (CG, CC, CD)
            self.action_execute()
            click = pygame.mouse.get_pressed()
            print(click)
            pygame.draw.rect(surface, self.couleur_click, (self.position, self.taille))
            self.message.afficher(surface)

        else:
            pygame.draw.rect(surface, self.couleur, (self.position, self.taille))
            self.message.afficher(surface)

        # implementation des actions ICI

    def action_execute(self):
        click = pygame.mouse.get_pressed()
        print(click)
        if click[0] == 1 and self.action is not None:
            print("Inside boucle")
            self.action()


