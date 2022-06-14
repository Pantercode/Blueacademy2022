# importando biblioteca
import pygame
# Iniciando o mp3
pygame.init()
# carregando a musica
pygame.mixer.music.load('cab.mp3')
# tocando musica
pygame.mixer.music.play()
# Espera o evento finalizar para encerrar a musica
pygame.event.wait()
print('Deu certo!!')