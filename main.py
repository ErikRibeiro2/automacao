from time import sleep
import pyautogui as pa # é nescessario ter esse pacote instalado no projeto (Documentação: )

# ATENÇÃO: Antes de executar o código, abra o paint e deixe a area de desejo no tamanho maximo
# Ao executar, você terá 5 segundos para colocar no paint, depois que fizer isso, não mecha no mouse.

distancia = 385 # distancia a percorrer
tira = 15 # tira uns valores da distancia

print("Iniciando desenho...")

sleep(5) #delay para você colocar o mouse no paint

pa.moveTo(240, 300), #ira mover o mouse para essa posicao


#inicio do desenho
while distancia > 0:
    pa.drag(distancia, 0, duration=0.15)  # direita
    distancia = distancia - tira
    pa.drag(0, distancia, duration=0.15)  # para baixo
    pa.drag(-distancia, 0, duration=0.15)  # para esquerda
    distancia = distancia - tira
    pa.drag(0, -distancia, duration=0.15)  # para cima

print("Desenho finalizado.")
