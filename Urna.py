#arrumar porcentagem
#adicionar time para cada validação   

def soma_ou_Troca(numeroVotos, opt):
    print(f"Confirma o candidato selecionado: (1)Sim (2)Não")
    confirma = int(input())
            
    if confirma == 1:
        match opt:
            case 10:
                opt = 1
                numeroVotos[opt] += 1
            case 20:
                opt = 2
                numeroVotos[opt] += 1
            case 30:
                opt = 3
                numeroVotos[opt] += 1
            
        return print('Voto válidado'), True
    
    else:
        return False

def opcao(candidatos, opt, numeroVotos):
    
    if opt in candidatos:
        print(candidatos[opt])
        return soma_ou_Troca(numeroVotos, opt)
    else:
        print("Voto nulo")
        numeroVotos[4] += 1
        return True

def exibirResultado(candidatos, numeroVotos, quantidadePessoas):
    numeroVotos.append(numeroVotos[0] + numeroVotos[4])
    total_votos = quantidadePessoas
    metade_votos = total_votos / 2
    multiplicador = 10
    
    if numeroVotos[5] >= metade_votos:
        print("Nova votação necessária (votos em branco/nulos é igual ou supera metade dos votos válidos)")
    else:
        print(f'Eleitores: {quantidadePessoas}')
        for i in range(4):
            porcentagem = (numeroVotos[i]*100)/total_votos
            if i == 0:
                print(f'Votos em branco: {numeroVotos[0]} {(numeroVotos[0]*100)/total_votos}%\nVotos nulos: {numeroVotos[4]} {(numeroVotos[0]*100)/total_votos}%')
            elif i > 0 and i <=3:
                print(f"{candidatos[(i)*multiplicador]}: {numeroVotos[i]}  {porcentagem}%")
                    
        for opt, votos in enumerate(numeroVotos[1:], start=1):       
            if votos >= metade_votos:
                print(f"{candidatos[opt*multiplicador]} venceu a eleição com {votos} votos. Obteve {(numeroVotos[i]*100)/total_votos}% de aprovação") #arrumar porcentagem
    
def votacao():
    candidatos = {0: "Voto em Branco", 10: "Antônio da Silva", 20: "José Nascimento", 30: "Paulo Cardos"}
    numeroVotos = [0, 0, 0, 0, 0]
    
    concluido = False
    
    print("Quantas pessoas irão votar?")
    quantidadePessoas = int(input())
    
    
    for _ in range(quantidadePessoas):
        concluido = False
        while not concluido:
            
            for num, name in candidatos.items():
                print(f'{num}: {name}')

            print("digite o código do candidato:")
            opt = int(input())  
                
            concluido = opcao(candidatos, opt, numeroVotos)
    
    exibirResultado(candidatos, numeroVotos, quantidadePessoas)

votacao()