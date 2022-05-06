#programa para rodar música
import pygame
#pode ser from pygame import mixer
pygame.mixer.init()
#carrega a musica
pygame.mixer.music.load('reboque.mp3')
pygame.mixer.music.play()
input('Agora vai')