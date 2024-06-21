
def soma_ou_Troca():
    confirma = int(input("Confirma o candidato selecionado: (1)Sim (2)Não "))
    
    if confirma == 1:
        soma += 1
    else:
        pass

def opcao(candidatos, opt):
    match opt:
        case "1":
            print(candidatos[opt])

def nomearCandidato(num, participantes):
    for i in range(num):
        participantes[i] = i
    return participantes

def exibirResultado(participantes, candidatos):
    print("digite o código ou o nome do candidato")
    opt = input()
    
    opcao(candidatos, opt)

def votacao():
    candidatos = {"1": "romar", "2": "romar", "3": "romar"}
    participantes = {}
    
    print("Quantas pessoas irão votar?")
    quantidadePessoas = int(input())
    
    nomearCandidato(quantidadePessoas, participantes)
    
    exibirResultado(participantes, candidatos)
    
    nulos()
    
    brancos()
    
    empate()
    removerPessoas()


votacao()