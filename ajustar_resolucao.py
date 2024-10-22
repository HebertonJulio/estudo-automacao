import os
import time
import pyautogui

# tempo de espera ate a execucao do script 
time.sleep(3)

# VAI PARA AREA DE TRABALHO 
pyautogui.moveTo(1918, 1057, duration=1.3)
pyautogui.click()
time.sleep(1)

# COLOCA O PONTEIRO NA AREA DE TRABALHO.
pyautogui.moveTo(1513, 493, duration=1.3)
pyautogui.click(button='right')
time.sleep(1)

# CLICA EM CIMA DE CONFIGURACOES DE EXIBICOES 
pyautogui.moveTo(1593, 713, duration=1.3)
pyautogui.click()
time.sleep(1)

# ROLA A ABA PARA BAIXO 
pyautogui.moveTo(1908, 989, duration=1.3)
pyautogui.click()
pyautogui.click()
time.sleep(1)

# CLICA NA RESOLUCAO DE TELA
pyautogui.moveTo(451, 607, duration=1.3)
pyautogui.click()
time.sleep(1)

# TROCA A RESOLUCAO PARA 1340 x 1080 
pyautogui.moveTo(439, 578, duration=1.3)
pyautogui.click()
time.sleep(1)

# CLICA EM MANTER CONFIRMACAO DE RESOLUCAO 
pyautogui.moveTo(805, 556, duration=1.3)
pyautogui.click()
time.sleep(1)

# CLICA EM CONFIGURACOES AVANCADAS DE TELA
pyautogui.moveTo(393, 924, duration=1.3)
pyautogui.click()
time.sleep(1)

# CLICA NA TAXA DE ATUALIZACAO DE HZ
pyautogui.moveTo(121, 686, duration=1.3)
pyautogui.click()
time.sleep(1)

# TROCA PARA 75HZ
pyautogui.moveTo(105, 721, duration=1.3)
pyautogui.click()
time.sleep(1)

# CLICA EM MANTER ALTERACOES 
pyautogui.moveTo(806, 556, duration=1.3)
pyautogui.click()
time.sleep(1)

# FECHA O GERENCIADOR DE RESOLUCOES
pyautogui.moveTo(1317, 12, duration=1.3)
pyautogui.click()
time.sleep(1)

# ABRIR O Winexp 
# os.startfile(r"c:\Users\Heberton\Desktop\folder\winexp\winexp.exe")
pyautogui.moveTo(35, 955, duration=1.3)
pyautogui.doubleClick()
time.sleep(3)


# ACEITAR ADMINISTRADOR 

pyautogui.moveTo(568, 658, duration=1.3)
pyautogui.click()
time.sleep(1.3)


# ROLA A BARRA DO WINEXP PARA BAIXO
pyautogui.moveTo(518, 188, duration=1.3)
pyautogui.click()
time.sleep(1)

# # CLICA DIVERSAS VEZES PARA IR PARA BAIXO
pyautogui.moveTo(518, 212, duration=1.3)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(518, 212, duration=1.3)
pyautogui.click()


# CLICA NO VALORANT 
pyautogui.moveTo(85, 201, duration=1.3)
pyautogui.doubleClick()
time.sleep(1.3)

# VAI NA ABA STYLE 
pyautogui.moveTo(342, 261, duration=1.3)
pyautogui.click()
time.sleep(1.3)

# DESMARCA A OPCAO WS_BORDER
pyautogui.moveTo(36, 401, duration=1.3)
pyautogui.click()
time.sleep(1.3)

# VAI PARA A ABA "Size & Position"
pyautogui.moveTo(108, 262, duration=1.3)
pyautogui.click()
time.sleep(1.3)

# MARCA A OPCAO "MAXIMIZED"
pyautogui.moveTo(272, 332, duration=1.3)
pyautogui.click()
time.sleep(1.3)











