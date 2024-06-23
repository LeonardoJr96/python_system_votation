# Simulador de Eleição

## Funcionamento do Programa

Este é um simulador de eleição desenvolvido em Python, onde os eleitores podem votar em candidatos ou optar por voto em branco ou nulo. O programa calcula e exibe os resultados da eleição, determinando se há um vencedor ou se será necessário realizar uma nova eleição.

### Inicialização

O programa inicia solicitando ao usuário o número de eleitores que irão participar da votação.

### Votação

- Para cada eleitor, o programa exibe os candidatos disponíveis, bem como a opção de voto em branco ou nulo.
- O eleitor digita o código do candidato ou da opção desejada (0 para voto em branco, 10, 20 ou 30 para os candidatos específicos).
- Após cada voto, o programa solicita uma confirmação do eleitor.

### Processamento de Votos

- Os votos são contabilizados em um vetor `numeroVotos`, onde cada posição corresponde a um tipo de voto (voto em branco, votos válidos para cada candidato, votos nulos).
- A função `soma_ou_Troca` processa o voto e retorna True se o voto foi confirmado, e False caso contrário.

### Exibição dos Resultados

- Após todos os eleitores votarem, o programa calcula a porcentagem de votos para cada categoria (votos válidos, votos em branco, votos nulos).
- Verifica se algum candidato obteve mais da metade dos votos válidos. Se sim, esse candidato é declarado vencedor.
- Caso contrário, se houver empate ou nenhum candidato atingir a maioria, o programa informa que não houve um vencedor claro e sugere uma nova eleição.

### Componentes do Programa

- **Funções Principais:**
  - `votacao()`: Inicia o processo de votação e chama as funções necessárias para processar os votos e exibir os resultados.
  - `opcao(num, candidatos, opt, numeroVotos)`: Permite ao eleitor escolher um candidato ou votar em branco/nulo.
  - `exibirResultado(candidatos, numeroVotos, quantidadePessoas)`: Calcula e exibe os resultados da eleição.

- **Funções de Apoio:**
  - `carregar()`: Simula um carregamento visual durante a votação.
  - `porcentagem(numeroVotos, candidatos, multiplicador, total_votos)`: Calcula e exibe a porcentagem de votos para cada categoria.

## Como Executar o Programa

1. **Pré-requisitos:**
   - Python 3.x instalado no seu sistema.

2. **Instruções:**
   - Clone o repositório ou baixe o arquivo `Urna.py` para o seu computador.
   - Abra um terminal ou prompt de comando na pasta onde o arquivo `Urna.py` está localizado.
   - Execute o programa digitando `python Urna.py` e siga as instruções exibidas no console para simular a eleição.

## Exemplo de Uso

### Console

```plaintext
Quantas pessoas irão votar?
5
0: Voto em Branco
10: Antônio da Silva
20: José Nascimento
30: Paulo Cardos
Eleitor 1, digite o código do candidato:
10
Antônio da Silva
Confirme o candidato selecionado: (1)Sim (2)Não
1
Voto válido para Antônio da Silva registrado.

Eleitor 2, digite o código do candidato:
20
José Nascimento
Confirme o candidato selecionado: (1)Sim (2)Não
1
Voto válido para José Nascimento registrado.

Eleitor 3, digite o código do candidato:
30
Paulo Cardos
Confirme o candidato selecionado: (1)Sim (2)Não
1
Voto válido para Paulo Cardos registrado.

Eleitor 4, digite o código do candidato:
0
Voto em Branco
Confirme o candidato selecionado: (1)Sim (2)Não
1
Voto em branco registrado.

Eleitor 5, digite o código do candidato:
15
Voto nulo

carregando...

Número de eleitores: 5

Votos em branco: 1 (20.00%)
Votos nulos: 1 (20.00%)
Antônio da Silva: 1  (20.00%)
José Nascimento: 1  (20.00%)

Total brancos/nulos: 2  (40.00%)

Não houve candidato vencedor – Será necessário nova eleição
