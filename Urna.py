
def soma_ou_Troca(numeroVotos, opt, concluido):
    print(f"Confirma o candidato selecionado: (1)Sim (2)Não")
    confirma = int(input())
    
    if confirma == 1:
        numeroVotos[int(opt)] += 1
        concluido = True
        return concluido
    else:
        concluido = False
        return concluido

def opcao(candidatos, opt, numeroVotos, concluido):
    opt = opt.strip()
    
    if opt in candidatos:
        print(candidatos[opt])
        return soma_ou_Troca(numeroVotos, opt, concluido)
    else:
        print("Voto nulo")
        numeroVotos[4] += 1
        return False

def exibirResultado(candidatos, numeroVotos, povo):
    numeroVotos.append(numeroVotos[0] + numeroVotos[4])
    total_votos = len(povo)
    metade_votos = total_votos / 2
    
    if numeroVotos[5] >= metade_votos:
        print("Nova votação necessária (votos em branco/nulos superam metade dos votos válidos)")
    else:
        for opt, votos in enumerate(numeroVotos[1:], start=1):
            if votos >= metade_votos:
                for i in range(3):
                    print(f'{candidatos[i+1]} : {numeroVotos[i+1]} votos')
                    if i == 3:
                        (f'{candidatos[i+2]} : {numeroVotos[i+2]} votos')
                print(f"{candidatos[str(opt)]} venceu a eleição com {votos} votos.")

def votacao():
    candidatos = {"0": "Voto em Branco", "1": "leonardo", "2": "jao", "3": "romar"}
    povo = {}
    numeroVotos = [0, 0, 0, 0, 0]
    
    concluido = False
    
    print("Quantas pessoas irão votar?")
    quantidadePessoas = int(input())
    
    for i in range(quantidadePessoas):
        print('Digite seu nome: ')
        povo[i] = input()
    
    while concluido == False:
        for _ in range(quantidadePessoas):
            print(f"{povo[_]} digite o código ou o nome do candidato:")
            opt = input().strip()
            opcao(candidatos, opt, numeroVotos, concluido)
    
    exibirResultado(candidatos, numeroVotos, povo)

votacao()