import pyautogui as spam
import time

limite = input('Número de mensagens:')
mensagem = input('Sua mensagem:')

a = 0

time.sleep(2)

while a<int(limite):
    spam.typewrite(mensagem)
    spam.press('Enter')

a+=1

# Comando feito por mim mesmo!
# Não precisa baixar as bibliotecas 'pyautogui' e 'time', elas ja são nativas do Python!
