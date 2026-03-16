fichas_rpg = [] #lista onde armazena as fichas dos personagens


def criar_ficha(): # função para criar as fichas

    nome = input('Digite o nome do seu personagem: ')
    classe = input('Digite a classe do seu personagem: ')
    nivel = input('Digite o nível do seu personagem: ')

    personagem = {"nome": nome, "classe": classe, "nivel": nivel}
    fichas_rpg.append(personagem)
    print('Ficha criada com sucesso!')


def ficha_disponivel():# função para verificar as fichas

    if not fichas_rpg:# Caso n tenha nenhuma ficha cadastrada, executa a mensagem
        print('\nNada cadastrado no momento')

    else:# Mostra as fichas e usa o for para enumerar as fichas cadastradas
        print('\n---------|Fichas cadastradas|---------- ')
        for i, f in enumerate(fichas_rpg):
            print(f"{i + 1}. Nome: {f['nome']} | Classe: {f['classe']} | Nível: {f['nivel']}")


def excluir_ficha():
    ficha_disponivel()  # Mostra as fichas primeiro

    # Quando não tem nenhuma ficha cadastrada
    if not fichas_rpg:
        print("Não há fichas cadastradas para excluir.")
        return

    #
    try:
        indice = int(input('\nDigite o número da ficha que deseja excluir: ')) - 1

        if 0 <= indice < len(fichas_rpg):
            removido = fichas_rpg.pop(indice)
            print(f"Personagem {removido['nome']} excluído com sucesso!")
        else:
            print("Número inválido! Esse índice não existe.")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")

def menu():
    while True:
        print('\n---------- Menu fichas de RPG ----------')
        print('1. Adicionar ficha de personagem')
        print('2. Ver fichas disponíveis')
        print('3. Excluir ficha personagem')
        print('4. Sair do programa')

        try:
            opcao = int(input('\nDigite a opção que deseja fazer: '))

            if opcao == 1:
                criar_ficha()

            elif opcao == 2:
                ficha_disponivel()

            elif opcao == 3:
                excluir_ficha()

            elif opcao == 4:
                print("\nSaindo...")
                break

            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Digite apenas números de 1 a 4.")

menu()
