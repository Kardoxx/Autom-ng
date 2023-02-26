#Kardo Tamm
import pygame
import sys

pygame.init()

#Pygame aeg
clock = pygame.time.Clock()

#Määrab display suuruse
screen = pygame.display.set_mode([640, 480])

punaneposx = 290
#Laeb mängu sinise auto pildi ja siis muudab pildi suurust funktsiooniga
sinine_auto = pygame.image.load("sinine_auto.png")
sinine_auto = pygame.transform.scale(sinine_auto, [60, 150])
sinine_posx, sinine_posy = 170, -210

#Laeb mängu sinise auto pildi ja siis muudab pildi suurust funktsiooniga
sinine_auto2 = pygame.image.load("sinine_auto.png")
sinine_auto2 = pygame.transform.scale(sinine_auto2, [60, 150])
sinine_posx2, sinine_posy2 = 420, -300

#Määrab kiiruse
kiirus = 3

#Skoori font on times new roman
score_font = pygame.font.SysFont("times New Roman", 30)

#Antud koodirida defineerib funktsiooni nimega skoor
def skoor(score):
    value = score_font.render("Sinu skoor: " + str(score), True, [0, 0, 0])
    screen.blit(value, [0, 0])

#Need koodiread määravad mängu põhiloogika - mängu tsükli. See käivitab mängu ja hoiab seda töös, kuni mängija lõpetab või jõuab mängu lõppu.
lopp_skoor = 0
mang_labi = False
while not mang_labi:
    clock.tick(60)

    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    if sinine_posy >= 480:
        sinine_posy = -210
        lopp_skoor += 1

    if sinine_posy2 >= 480:
        sinine_posy2 = -300
        lopp_skoor += 1


    screen.blit(sinine_auto, (sinine_posx, sinine_posy))
    sinine_posy += kiirus
    pygame.display.flip()

    screen.blit(sinine_auto2, (sinine_posx2, sinine_posy2))
    sinine_posy2 += kiirus
    pygame.display.flip()

    #laeb mängu tausta pildi nimega "taust.jpg"" ning seejärel muudab selle suurust
    background = pygame.image.load("taust.jpg")
    background = pygame.transform.scale(background, [640, 480])
    screen.blit(background, [0, 0])

  #laeb mängu punase auto pildi nimega "punane_auto.png" ning seejärel muudab selle suurust
    punane_auto = pygame.image.load("punane_auto.png")
    punane_auto = pygame.transform.scale(punane_auto, [60, 150])
    screen.blit(punane_auto, [punaneposx, 310])

    key = pygame.key.get_pressed()  # saame vajutatud klahvi
    if key[pygame.K_LEFT]:  # kui vasak klahv
        punaneposx -= 5  # liigutame autot vasakule
    if key[pygame.K_RIGHT]:  # kui parem klahv
        punaneposx += 5  # liigutame autot paremale

    # Näitab sinu lõppskoori
    if (punaneposx >= sinine_posx and punaneposx <= sinine_posx + 60) or (
            punaneposx + 60 >= sinine_posx and punaneposx + 60 <= sinine_posx + 60):
        if sinine_posy >= 310 and sinine_posy <= 460:
            mang_labi = True
            print("Mäng läbi! Sinu skoor: " + str(lopp_skoor))

#Näitab sinu lõppskoori
    if (punaneposx >= sinine_posx2 and punaneposx <= sinine_posx2 + 60) or (
            punaneposx + 60 >= sinine_posx2 and punaneposx + 60 <= sinine_posx2 + 60):
        if sinine_posy2 >= 310 and sinine_posy2 <= 460:
            mang_labi = True
            print("Mäng läbi! Sinu skoor: " + str(lopp_skoor))
#Prindib lõppskoori
    skoor(lopp_skoor)


#Lahkub pygamest
pygame.quit()