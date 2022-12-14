# -*- coding: utf-8 -*-

estados = input().split(" ")
simbalf = input().split(" ")
qtdtrans = int(input())

afd = {}

for estado in estados:
    afd[estado] = {}

for i in range(0, qtdtrans):
    ei, ec, ef = input().split(" ")
    if ec not in afd[ei]:
        afd[ei][ec] = [ef]
    else:
        afd[ei][ec].append(ef)

estado_inicial = input()
estado_f = input().split(" ")
palavras = input().split(" ")

estados_finais = {}
for k in estado_f:
    estados_finais[k] = 1

for palavra in palavras:
    estados_atuais = [estado_inicial]
    estado_final = 0

    for char in palavra:
        novo_estados_atuais = []
        for estado in estados_atuais:
            if(afd[estado].get(char)):
                for novo_estado in afd[estado][char]:
                    if(novo_estado not in novo_estados_atuais):
                        novo_estados_atuais.append(novo_estado)
        estados_atuais = novo_estados_atuais

    for estado in estados_atuais:
        if(estados_finais.get(estado)):
            estado_final = 1
    if(estado_final == 1):
        print('S')
    else:
        print('N')
