import tkinter as tk
from tkinter import messagebox
import random


tentativas = 0
adivinhou = False
numero_secreto = random.randint(1, 100)
print('Bem vindo ao jogo de advinhação!')
print('Tente advinhar o numero de 1 a 100')

while not adivinhou :
    palpite = int(input('Digite o seu palpite'))
    tentativas += 1

    if palpite < numero_secreto:
        print('O seu palpite foi muito baixo')
    elif palpite > numero_secreto :
        print("Seu palpite é muito alto.")
    else:
        adivinhou = True
        print('Parabens, voce advinhou o numero em {} tentativas'.format(tentativas))
