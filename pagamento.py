#Declarar variáveis
funcionario:str
valorHora:float
horasTrabalhadas:int
pagamentoFuncionario:float

try:
    #Entrada de dados
    funcionario = input("Digite seu nome")
    valorHora = float(input("Valor de sua hora"))
    horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas"))


    #Processamento de dados
    pagamento = (valorHora*horasTrabalhadas)

    #Saida de dados
    print(f"O valor do pagamento de {funcionario} é R$ : + {pagamento:.2f}")
except: #Somente excepot sem nenhum type ou value Error é valido para tudo
    print("Valor inválido, tente novamente")      