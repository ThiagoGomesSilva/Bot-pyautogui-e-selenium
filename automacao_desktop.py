# Toda automação no seu computador utilizamos o pyautogui


# Passo a passo do que fazer
'''
Passo 1 = ir no windows e digitar na barra de busca login.xlsx
passo 2 = preencher o login
passo 3 = preencher a senha
passo 4 = clicar em fazer login
'''


# Biblioteca do pyautogui - Serve para automatizar programas/arquivos no seu computador
import pyautogui

import time

pyautogui.PAUSE = 2 # Esse comando em resumo esta dizendo que para cada comando abaixo o programa vai esperar 2 segundos para que o próximo comando seja executado

pyautogui.press('win') # o comando press serve para pressionar, e dentro dos parenteses inserimos a tecla do teclado que queremos que seja pressionada
pyautogui.write('loginautomacao') # o comando write "escrever" serve para que essa automação escreva o que passamos dentro dos parenteses, nesse caso o arquivo excel.
pyautogui.press('backspace') # o comando press serve para pressionar, e dentro dos parenteses inserimos a tecla do teclado que queremos que seja pressionada
pyautogui.press('enter') # o comando press serve para pressionar, e dentro dos parenteses inserimos a tecla do teclado que queremos que seja pressionada

pyautogui.click(x=693, y=468) # Clicando em login
pyautogui.write('thiago')

pyautogui.click(x=653, y=506) # Clicando em senha
pyautogui.write('123456')

pyautogui.click(x=546, y=614) # Clicando em fazer login

time.sleep(10)
pyautogui.click(x=1597, y=206) # Fechando programa clicando no x
pyautogui.click(x=956, y=556) # Fechando programa clicando no não salvar


# time.sleep(3)
# pyautogui.position()


