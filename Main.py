import csv
import os
from ListaSE import ListaSE
from BinaryTree import BinaryTree

def read_data_from_file(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Pular a linha de cabeçalho
        for row in csv_reader:
            if len(row) != 2:
                print(f"Linha inválida no arquivo CSV: {row}")
                continue
            try:
                id = int(row[0])
                name = row[1]
                data.append((id, name))
            except ValueError as e:
                print(f"Erro ao converter linha {row}: {e}")
    return data

def insert_into_file(file_path, id, name):
    with open(file_path, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([id, name])

def prompt_user_for_data():
    while True:
        try:
            id = int(input("Digite o ID: "))
            name = input("Digite o nome: ")
            return id, name
        except ValueError:
            print("ID deve ser um número inteiro. Tente novamente.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Crie instâncias da lista e da árvore
    lista = ListaSE()
    arvore = BinaryTree()

    # Leia os dados do arquivo
    file_path = 'data.csv'
    data = read_data_from_file(file_path)

    # Insira os dados na lista e na árvore
    for id, name in data:
        lista.insert(id, name)
        arvore.insert(id, name)

    while True:
        clear_console()
        # Exiba o menu de opções
        print("\nMenu:")
        print("1. Exibir lista")
        print("2. Inverter lista")
        print("3. Inserir novo elemento")
        print("4. Ordenar lista por ID")
        print("5. Ordenar lista por Nome")
        print("6. Consultar por ID na árvore")
        print("7. Consultar por ID na lista desorganizada")
        print("8. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            # Exiba a lista
            clear_console()
            print("Lista atual:")
            lista.display()
            input("Pressione Enter para continuar...")
        elif choice == '2':
            # Inverta a lista
            clear_console()
            lista.reverse()
            print("Lista invertida:")
            lista.display()
            input("Pressione Enter para continuar...")
        elif choice == '3':
            # Insira um novo registro
            clear_console()
            new_id, new_name = prompt_user_for_data()
            insert_into_file(file_path, new_id, new_name)
            lista.insert(new_id, new_name)
            arvore.insert(new_id, new_name)
            print(f"Elemento com ID {new_id} e nome {new_name} foi inserido.")
            input("Pressione Enter para continuar...")
        elif choice == '4':
            # Ordenar a lista por ID
            clear_console()
            lista.bubble_sort(by='id')
            print("Lista ordenada por ID:")
            lista.display()
            input("Pressione Enter para continuar...")
        elif choice == '5':
            # Ordenar a lista por Nome
            clear_console()
            lista.bubble_sort(by='name')
            print("Lista ordenada por Nome:")
            lista.display()
            input("Pressione Enter para continuar...")
        elif choice == '6':
            # Consultar por ID na árvore
            clear_console()
            try:
                search_id = int(input("Digite o ID para consulta: "))
                result, steps = arvore.search(search_id)
                if result:
                    print(f"Elemento encontrado na árvore: ID {result.id}, Nome {result.name}")
                else:
                    print(f"Nenhum elemento encontrado na árvore com ID {search_id}.")
                print(f"Número de passos na árvore: {steps}")
            except ValueError:
                print("ID deve ser um número inteiro. Tente novamente.")
            input("Pressione Enter para continuar...")
        elif choice == '7':
            # Consultar por ID na lista desorganizada
            clear_console()
            try:
                search_id = int(input("Digite o ID para consulta: "))
                result, steps = lista.search(search_id)
                if result:
                    print(f"Elemento encontrado na lista: ID {result.id}, Nome {result.name}")
                else:
                    print(f"Nenhum elemento encontrado na lista com ID {search_id}.")
                print(f"Número de passos na lista: {steps}")
            except ValueError:
                print("ID deve ser um número inteiro. Tente novamente.")
            input("Pressione Enter para continuar...")
        elif choice == '8':
            # Sair do loop
            break
        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
