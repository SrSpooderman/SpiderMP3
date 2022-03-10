#importaciones
import this
import pygame
from pygame.locals import *
from pygame import mixer
import os
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
#iniciacion de programa
pygame.init()
pygame.font.init()
mixer.init()
fuente_letra = pygame.font.SysFont('Comic Sans MS', 10)
#variables de pygame
run= True
WIDTH = 700 
HEIGHT = 400
PANTALLA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpiderMP3")
#load sprites
    #fondo
fondo= pygame.image.load("assets/fondo.png")
    #laterales
lateral_X= pygame.image.load("assets/lateral_x.png")
lateral_Y= pygame.image.load("assets/lateral_y.png")
    #imagen
panel_imagen= pygame.image.load("assets/panel_imagen.png")
    #panel elector cancion
panel_elector_canciones= pygame.image.load("assets/panel_e_canciones.png")
    #panel elector imagen
panel_elector_imagen= pygame.image.load("assets/panel_e_imagen.png")
    #panel de pausa, avanzar, play etc
panel_botones_canciones= pygame.image.load("assets/panel_botones_canciones.png")
    #logo
logo= pygame.image.load("assets/logo.png")
    #botones play y pausa
play= pygame.image.load("assets/play.png")
    #boton de inserta musica
music_button= pygame.image.load("assets/music_boton.png")
    #boton de inserta lista de musica
list_button= pygame.image.load("assets/list_boton.png")
    #boton de insertar imagen
image_button= pygame.image.load("assets/image_boton.png")
#load hitboxes
play_hbx = pygame.Rect(450, 120, 100, 100) #boton de pausa y play
music_button_hbx = pygame.Rect(40, 324, 100, 50) #Boton de elegir cancion
list_button_hbx= pygame.Rect(200, 324, 100, 50) #Boton de elegir lista
image_button_hbx= pygame.Rect(425, 300, 150, 40) #Boton de elegir imagen
#generate pantalla inicial
PANTALLA.blit(fondo, (0, 0))
PANTALLA.blit(lateral_X, (0, 0))
PANTALLA.blit(lateral_X, (0, 380))
PANTALLA.blit(lateral_Y, (0,0))
PANTALLA.blit(lateral_Y, (680,0))
PANTALLA.blit(panel_imagen, (20, 20))
PANTALLA.blit(panel_elector_canciones, (20, 320))
PANTALLA.blit(panel_elector_imagen, (320, 293))
PANTALLA.blit(panel_botones_canciones, (320, 70))
PANTALLA.blit(logo, (320, 20))
PANTALLA.blit(play, (450,120))
PANTALLA.blit(music_button, (40, 324))
PANTALLA.blit(list_button, (200, 324))
PANTALLA.blit(image_button, (425, 300))
#Main
while run:
    music=mixer.music.get_busy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_hbx.collidepoint(mouse_pos):
                    if music==True:
                        mixer.music.pause()
                        play= pygame.image.load("assets/pause.png")
                        PANTALLA.blit(play, (450,120))
                    if music==False:
                        mixer.music.unpause()
                        play= pygame.image.load("sprites/play.png")
                        PANTALLA.blit(play, (450,120))
                if music_button_hbx.collidepoint(mouse_pos):
                    cancion=askopenfilename(filetypes=[('audio', '*.mp3')])
                    if len(cancion) == 0:
                        pass
                    else:
                        mixer.music.load(cancion)
                        mixer.music.play()
                if list_button_hbx.collidepoint(mouse_pos):
                    print("boton de lista de cancion")
                if image_button_hbx.collidepoint(mouse_pos):
                    imagen= askopenfilename(filetypes=[('image', '*.jpg')])
                    if len(imagen) == 0:
                        pass
                    else:
                        print(imagen)
                        imagen_x= pygame.image.load(imagen)
                        imagen_x_T= pygame.transform.scale(imagen_x, [300, 300])
                        PANTALLA.blit(imagen_x_T, (20, 20))
    pygame.display.update()