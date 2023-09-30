# Passo a passo do projeto
# Passo 1: Entrar na pagina
# https://adrianarodriguesa.github.io/projeto_matrix/
# Passo 2: Trocar tema para escuro
# Passo 3: Digitar nome, e-mail, mensagem e enviar
# Passo 4: Aguardar a pagina resposta
# Passo 5: voltar para a pagina principal

# bibliotecas:
import pyautogui
import time
    
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
# no pyautogui.hotkey("ctrl", "c") para teclar duas tecla por exemplo, ou mais


# para pausar tudo
pyautogui.PAUSE = 0.5

# abrir menu windows e o chrome
pyautogui.press ("win") 
pyautogui.write("chrome")
pyautogui.press("enter")
# no nosso note precisamos colocar tempo antes de digitar pois estava abrir edge
time.sleep(5)
#Passo 1
link = "https://adrianarodriguesa.github.io/projeto_matrix/"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(9)

# Passo 2: 
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
# Passo 3:
pyautogui.write("Nome Sobrenome")
pyautogui.press("tab")
pyautogui.write("email_teste@teste.com") 
pyautogui.press("tab")
pyautogui.write("Mensagem codificada")
pyautogui.press("tab")
pyautogui.press("enter")
# Passo 4:
time.sleep(9)
pyautogui.press("tab")
pyautogui.press("enter")
# Passo 5:
pyautogui.press("tab")
pyautogui.press("enter")