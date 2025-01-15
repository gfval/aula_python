"""
montante = input("Qual o valor do montante? ")
respostas_validas = (range(5000, 10000))
respostas_invalidas = (range(0, 5000))

try:
    montante = float(montante)  

    def saudacaop():
        print('Olá, tudo bem?')
        print("Aceito a oferta!")

    def saudacaon():
        print('Olá, tudo bem?')
        print("Não aceito a oferta!")

    if montante > 5000.00:
        saudacaop()
    else:
        saudacaon()

except ValueError:
    print("Por favor, insira um número válido.")
    

funcoes serve para organizar o código e reutilizar o código
alem de facilitar a manutenção do código e fazer uso do DRY (Don't Repeat Yourself)

"""

user = input("Qual o seu nome? ")
montante = input("Qual o valor do montante? ")
respostas_validas = range(5000, 100000)  # Intervalo de respostas válidas (5000 a 100000)
respostas_invalidas = range(0, 5000)    # Intervalo de respostas inválidas (abaixo de 5000)

def saudacaop(user_name: str):
    print(f'Olá, tudo bem {user_name}?')
    print(f"Aceito a oferta {user_name}!")

def saudacaon(user_name: str):
    print(f'Olá, tudo bem {user_name}?')
    print(f"Nao Aceito a oferta {user_name}!")

while True:

    try:
        montante = float(montante)  # Converte a entrada para número

        if montante in respostas_validas:
            saudacaop(user)
            break  # Sai do loop após resposta válida
        elif montante in respostas_invalidas:
            saudacaon(user)
            break  # Sai do loop após resposta inválida
    except ValueError:
        print("Por favor, insira um número válido.")
