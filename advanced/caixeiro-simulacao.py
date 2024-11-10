# Programa: Simulação da Estratégia Reducionista no Problema do Caixeiro Viajante
#
# Autor: Odin Oliveira                      
# Revisor: 
# Data:06/02/2023
#
# Objetivo: Simulação de tempo que o computador que está executando o programa
# levaria para calcular algumas rotas para o caixeiro viajante sem
# utilizar Otimização Combinatória 
#
# Calcula o tempo que o processador da máquina leva para fazer 10 milhões
# de adições, cada edição é o calculo de um caminho (ligação entre duas
# cidade)

import time

tempo = time.time()
i = sum(range(1, 10000000))
tempo = time.time() - tempo
print("Tempo para processar 10 milhões de adições (segundos): ", tempo)
adicoes = 10000000 / tempo
print("Adições por segundo: ", int(adicoes))

cidades = [5, 10, 15, 20, 25]
for contador in cidades:
    print("\nCidades", contador)
    rotas_seg = (adicoes / (contador - 1))
    print("Rotas por segundo: ", int(rotas_seg))
    rotas = 1
    for i in range(2, contador):
        rotas *= i
    print("Rotas possíveis: ", rotas)
    tempo_calculo = rotas / rotas_seg
    if tempo_calculo < 1:
        print("Tempo para cálculo: ", int(tempo_calculo * 1000), " milisegundos")
    elif tempo_calculo < 60:
        print("Tempo para cálculo: ", int(tempo_calculo), " segundos")
    elif tempo_calculo < 3600:
        print("Tempo para cálculo: ", int(tempo_calculo / 60), " minutos")
    elif tempo_calculo < 86400:
        print("Tempo para cálculo: ", int(tempo_calculo / 3600), " horas")
    else:
        print("Tempo para cálculo: ", int(tempo_calculo / 86400), " dias")