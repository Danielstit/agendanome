
lista_de_contato = []  
while True:
    
    def adicionarcontato():
        contato = input("\nInforme o nome que deseja adicionar: \n")
        lista_de_contato.append(contato)
    def remover_contato():
        
        if len(lista_de_contato) == 0:
            print("A lista de contatos está vazia. Não há nada para remover.")
            return
        try:
            removercontato = int(input("Informe o índice que você quer remover: ")) 
            if 0 <= removercontato < len(lista_de_contato):
                lista_de_contato.pop(removercontato)  
                print("Contato removido com sucesso!")
            else:
                print("Índice inválido! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, informe um número válido.")
    def listar_contato():
        print("contatos listados:\n")
        if len(lista_de_contato) == 0:
            print("lista de contatos vazia!!")
        for indice, contato in enumerate(lista_de_contato):
            print(indice,contato)
    try: 
        validador = int(input("\ninforme uma das seguintes opções: [1]Adicionar [2] remover [3] listar [4]Sair\n"))
    except:
        print("valor informado é inválido. Por favor, informe um valor válido!!\n")
        continue
    if validador == 1: 
        adicionarcontato()
    elif validador==2:
        remover_contato()
    elif validador == 3:
        listar_contato()
    elif validador == 4:
        listar_contato()
    break
