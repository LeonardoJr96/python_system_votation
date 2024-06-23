
#adicionar time para cada validação  
import time

def carregar():
    print('\ncarregando...\n')
    time.sleep(2)
 
def porcentagem(numeroVotos, candidatos, multiplicador, total_votos):
    print(f"Número de eleitores: {total_votos}\n")
    for i in range(4):
        var_porcentagem = (numeroVotos[i]*100)/total_votos
        if i == 0:
            print(f'Votos em branco: {numeroVotos[i]} ({var_porcentagem:.2f}%)\nVotos nulos: {numeroVotos[4]} ({var_porcentagem:.2f}%)')
        elif i > 0 and i <= 3:
            print(f"{candidatos[i*multiplicador]}: {numeroVotos[i]}  ({var_porcentagem:.2f}%)")
            
    print(f"\nTotal brancos/nulos: {numeroVotos[5]}  ({(numeroVotos[5]*100)/total_votos:.2f}%)")

    
def soma_ou_Troca(num, numeroVotos, opt):
    print(f"Eleitor {num+1}, confirme candidato selecionado: (1)Sim (2)Não")
    confirma = int(input())
            
    if confirma == 1:
        match opt:
            case 0:
                numeroVotos[opt] += 1
                carregar()
                return print('\nVoto em branco\n'), True
            case 10:
                opt = 1
                numeroVotos[opt] += 1
                carregar()
                return print('\nVoto válidado\n'), True
            case 20:
                opt = 2
                numeroVotos[opt] += 1
                carregar()
                return print('\nVoto válidado\n'), True
            case 30:
                opt = 3
                numeroVotos[opt] += 1
                carregar()
                return print('\nVoto válidado\n'), True
    
    else:
        carregar()
        return False

def opcao(num, candidatos, opt, numeroVotos):
    
    if opt in candidatos:
        print(f'\n{candidatos[opt]}')
        return soma_ou_Troca(num, numeroVotos, opt)
    else:
        print("\nVoto nulo\n")
        numeroVotos[4] += 1
        carregar()
        return True

def exibirResultado(candidatos, numeroVotos, quantidadePessoas):
    
    lista_repeticao = []
    
    numeroVotos[5] = int(numeroVotos[0] + numeroVotos[4])
    total_votos = quantidadePessoas
    metade_votos = total_votos / 2
    multiplicador = 10
    
    verifica_repeticao = max(numeroVotos[1:4])
    
    for _ in range(total_votos):
        lista_repeticao.append(verifica_repeticao)
    
    if len(lista_repeticao) > 1:
        porcentagem(numeroVotos, candidatos, multiplicador, total_votos)
        print("\nNão houve candidato vencedor – Será necessário nova eleição")
    else:
        if numeroVotos[5] >= metade_votos:
            porcentagem(numeroVotos, candidatos, multiplicador, total_votos)
            print("\nNão houve candidato vencedor – Será necessário nova eleição")
        else:
            print(f'\nEleitores: {quantidadePessoas}')
            
            porcentagem(numeroVotos, candidatos, multiplicador, total_votos)
                        
            for opt, votos in enumerate(numeroVotos[1:], start=1):       
                if votos >= metade_votos:
                    print(f"\n{candidatos[opt*multiplicador]} venceu a eleição com {votos} votos. Obteve {(numeroVotos[opt]*100)/total_votos:.2f}% de aprovação")
    
def votacao():
    candidatos = {0: "Voto em Branco", 10: "Antônio da Silva", 20: "José Nascimento", 30: "Paulo Cardos"}
    numeroVotos = [0, 0, 0, 0, 0, 0]
    
    concluido = False
    
    print("Quantas pessoas irão votar?")
    quantidadePessoas = int(input())
    
    
    for _ in range(quantidadePessoas):
        concluido = False
        while not concluido:
            
            for num, name in candidatos.items():
                print(f'{num}: {name}')

            print(f"Eleitor {_+1}, digite o código do candidato:")
            opt = int(input())  
                
            concluido = opcao(_, candidatos, opt, numeroVotos)
            
    carregar()
    
    exibirResultado(candidatos, numeroVotos, quantidadePessoas)

votacao()