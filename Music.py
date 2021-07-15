import pygame


class Music:
    def __init__(self):
        pygame.mixer.init()
        self.select_case = pygame.mixer.Sound("sons/clic.wav")
        self.takeGraine = pygame.mixer.Sound("sons/handle.wav")
        self.dropGraine = pygame.mixer.Sound("sons/drop.wav")

        # self.sonsDeFond = pygame.mixer.music.load("musique/main.mp3")
        self.sonPerdu = pygame.mixer.music.load("musique/perdu.mp3")
        self.sonGagne = pygame.mixer.music.load("musique/gagne.mp3")
        pygame.mixer.music.set_volume(0.2)

    def play_sonDeFond(self):
        pygame.mixer.music.load("musique/main.mp3")
        pygame.mixer.music.play(-1)

    def play_sonPerdu(self):
        pygame.mixer.music.load("musique/perdu.mp3")
        pygame.mixer.music.play()

    def play_sonGagne(self):
        pygame.mixer.music.load("musique/gagne.mp3")
        pygame.mixer.music.play()

    def play_sonIntro(self):
        pygame.mixer.music.load("musique/intro.mp3")
        pygame.mixer.music.play(-1)

    def play_sonNull(self):
        pygame.mixer.music.load("musique/intro.mp3")
        pygame.mixer.music.play()

    def stop_musique(self):
        pygame.mixer.music.stop()

    def play_select_case(self):
        pygame.mixer.Sound.play(self.select_case)

    def play_takeGraine(self):
        pygame.mixer.Sound.play(self.takeGraine)

    def play_dropGraine(self):
        pygame.mixer.Sound.play(self.dropGraine)

    def stop_select_case(self):
        pygame.mixer.Sound.play(self.select_case)

    def stop_takeGraine(self):
        pygame.mixer.Sound.play(self.takeGraine)

    def stop_dropGraine(self):
        pygame.mixer.Sound.play(self.dropGraine)

