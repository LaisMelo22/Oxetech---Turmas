import pyautogui
import time

# Acessando o Chrome e Gmail
pyautogui.press('win')
time.sleep(1)
pyautogui.write('Chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('gmail.com')
time.sleep(1)
pyautogui.press('enter')

# Aguarde um pouco para você poder preparar a tela
time.sleep(5)   

# Define o assunto e o corpo do e-mail
assunto = "Assunto do e-mail"
corpo = "Este é o corpo do e-mail.\nalo"

# Clicando em 'Escrever' e digitando email destinatário
pyautogui.click(x=144, y=190) 
time.sleep(1)
pyautogui.write('elmb@ic.ufal.br')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Escrevendo assunto do email
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(assunto)

# Escrevendo corpo do email
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(corpo)

# Enviar e-mail
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')