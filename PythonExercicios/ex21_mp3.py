"""
ex21- Faça um programa em Python que abra e reproduza o áudio de arquuivo mp3
"""
import pygame
pygame.init()
pygame.mixer.music.load('saiarodada.mp3')
pygame.mixer.music.play()
pygame.event.wait()