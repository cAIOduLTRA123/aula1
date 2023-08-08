def mostrar_lista(lista):
    print("Lista atual:")
    for i, item in enumerate(lista):
        print(f"{i + 1}. {item}")
    print()

def adicionar_item(lista, item):
    lista.append(item)
    print(f"{item} foi adicionado à lista.")

def editar_item(lista, indice, novo_valor):
    if indice >= 0 and indice < len(lista):
        lista[indice] = novo_valor
        print(f"Item {indice + 1} editado para: {novo_valor}.")
    else:
        print("Índice inválido!")

def apagar_item(lista, indice):
    if indice >= 0 and indice < len(lista):
        item_removido = lista.pop(indice)
        print(f"Item {indice + 1} removido: {item_removido}.")
    else:
        print("Índice inválido!")

lista = []

while True:
    print("Opções:")
    print("1. Mostrar lista")
    print("2. Adicionar item")
    print("3. Editar item")
    print("4. Apagar item")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        mostrar_lista(lista)
    elif escolha == "2":
        item = input("Digite o item a ser adicionado: ")
        adicionar_item(lista, item)
    elif escolha == "3":
        mostrar_lista(lista)
        indice = int(input("Digite o índice do item a ser editado: ")) - 1
        novo_valor = input("Digite o novo valor: ")
        editar_item(lista, indice, novo_valor)
    elif escolha == "4":
        mostrar_lista(lista)
        indice = int(input("Digite o índice do item a ser apagado: ")) - 1
        apagar_item(lista, indice)
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Digite novamente.")
