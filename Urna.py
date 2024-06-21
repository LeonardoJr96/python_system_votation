
def soma_ou_Troca(numeroVotos, opt):
    while True:
        print("Confirma o candidato selecionado: (1)Sim (2)Não")
        confirma = int(input())
    
        if confirma == 1:
            numeroVotos[int(opt)] = numeroVotos[int(opt)] + 1
            break
        else:
             return True

def opcao(candidatos, opt, numeroVotos):
    opt.strip()
    
    if opt in candidatos:
        print(candidatos[opt])
        return soma_ou_Troca(numeroVotos, opt)
    else:
        opt = 5
        print("Voto nulo")
        return soma_ou_Troca(numeroVotos, opt)

def nomearCandidato(num, participantes):
    for i in range(num):
        participantes[i] = i
    return participantes

def exibirResultado(participantes, candidatos, numeroVotos):
    print("digite o código ou o nome do candidato")
    opt = str(input())
    
    
    opcao(candidatos, opt, numeroVotos)

def votacao():
    candidatos = {"0": "Voto em Branco", "1": "romar", "2": "romar", "3": "romar"}
    participantes = {}
    numeroVotos = [0, 0, 0, 0, 0]
    
    print("Quantas pessoas irão votar?")
    quantidadePessoas = int(input())
    
    nomearCandidato(quantidadePessoas, participantes)
    
    exibirResultado(participantes, candidatos, numeroVotos)


votacao()