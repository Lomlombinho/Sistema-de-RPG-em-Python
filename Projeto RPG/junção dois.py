fichas_rpg = [] #lista onde armazena as fichas dos personagens


def criar_ficha(): # função para criar as fichas

    nome = input('Digite o nome do seu personagem: ')
    classe = input('Digite a classe do seu personagem: ')
    nivel = int(input('Digite o nível do seu personagem: '))

    try:
        v_forca = int(input('Digite o valor de sua força: '))
        v_magia = int(input('Digite o valor de sua magia: '))
        v_agilidade = int(input('Digite o valor de sua agilidade: '))
    except ValueError:
        print('Apenas digite números caro gafanhoto')
        return

    personagem= {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
        "forca": v_forca,
        "magia": v_magia,
        "agilidade": v_agilidade
    }


    fichas_rpg.append(personagem)
    print('Ficha criada com sucesso!')


def ficha_disponivel():# função para verificar as fichas

    if not fichas_rpg:# Caso n tenha nenhuma ficha cadastrada, executa a mensagem
        print('\nNada cadastrado no momento')

    else:# Mostra as fichas e usa o for para enumerar as fichas cadastradas
        print('\n---------|Fichas cadastradas|---------- ')
        for i, f in enumerate(fichas_rpg):
            print(
                f"{i + 1}. Nome: {f['nome']} | Classe: {f['classe']} | Nível: {f['nivel']} | Força: {f['forca']} | Magia: {f['magia']} | Agilidade: {f['agilidade']}")


def excluir_ficha():
    ficha_disponivel()  # Mostra as fichas primeiro

    # Quando não tem nenhuma ficha cadastrada
    if not fichas_rpg:
        print("Não há fichas cadastradas para excluir.")
        return

    #Exclui as ficha que vc criou
    try:
        indice = int(input('\nDigite o número da ficha que deseja excluir: ')) - 1

        if 0 <= indice < len(fichas_rpg):
            removido = fichas_rpg.pop(indice)
            print(f"Personagem {removido['nome']} excluído com sucesso!")
        else:
            print("Número inválido! Esse índice não existe.")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")

#Menu onde executará os comandos
def menu():
    while True:
        print('\n---------- Menu fichas de RPG ------------')
        print('1. Adicionar ficha de personagem')
        print('2. Ver fichas disponíveis')
        print('3. Excluir ficha personagem')
        print('4. Começar batalha para testar ficha')
        print('5. Sair do programa')

#estrutura de escolha das opções
        try:
            opcao = int(input('\nDigite a opção que deseja fazer: '))

            if opcao == 1:
                criar_ficha()

            elif opcao == 2:
                ficha_disponivel()

            elif opcao == 3:
                excluir_ficha()

            elif opcao == 4:
                menu_batalha()

            elif opcao == 5:
                print("\nSaindo...")
                break

            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Digite apenas números de 1 a 5.")


#usada pra gerar as estatísticas dos inimigos
import random

#função pra calcular poder total do nosso personagem oreia seca
def calculo_poder(v_forca, v_magia, v_agilidade):
    poder_total = (v_forca * 2) + v_magia + v_agilidade
    return poder_total

def escolher_ficha():
    ficha_disponivel()

    if not fichas_rpg:
        return None

    try:
        escolha = int(input("\nEscolha o número da ficha: ")) - 1

        if 0 <= escolha < len(fichas_rpg):
            return fichas_rpg[escolha]
        else:
            print("Escolha inválida.")
            return None

    except ValueError:
        print("Digite um número válido.")
        return None

#função de pra definir o ranking de poder do personagem oreia seca
def definir_ranking(poder):
    if poder < 100:
        return 'Bronze'

    elif poder < 200:
        return 'Prata'

    elif poder < 500:
        return 'Ouro'

    else:
        return 'Lendário'

#função pra calcular o dano do oreia seca
def calcular_dano(ataque, defesa):
    dano = ataque - defesa
    dano = max(0, dano)
    return dano

#funçaõ pra começar a rinha de personagens
def sistema_batalha(poder_total, v_agilidade):
    vida_player = 100
    inimigos_mortos = 0
    jogando = True

#laço que repete as rinhas de personagens
    while vida_player > 0 and jogando:

#gera vida, ataque e defesa aleatória do nosso inimigo
        vida_inimigo = random.randint(150, 200)
        ataque_inimigo = random.randint(15, 25)
        defesa_inimigo = random.randint(5, 15)

        print(f"\n--- Inimigo {inimigos_mortos + 1} apareceu! ---")

#mostra quanto vc tomou de dano ou dano crítico
        while vida_inimigo > 0 and vida_player > 0:
            dano_causado = calcular_dano(poder_total, defesa_inimigo)

            if input("Seu ataque foi crítico? (s/n): ").lower() == 's':
                dano_causado = calcular_dano(poder_total*2, defesa_inimigo)
            vida_inimigo -= dano_causado
            print(f"Você causou {dano_causado} de dano! Inimigo: {max(0, vida_inimigo)} HP")

            if vida_inimigo <= 0:
                inimigos_mortos += 1
                print("Inimigo derrotado!")
                break

            dano_recebido = calcular_dano(ataque_inimigo, v_agilidade // 2)
            vida_player -= dano_recebido
            print(f"Você sofreu {dano_recebido} Dano | Seu HP: {max(0, vida_player)}")

#caso queira continuar ou não
        if vida_player > 0:
            continuar = input("\nDeseja ir para a próxima luta? (s/n): ")
            if continuar.lower() != 's':
                jogando = False
        else:
            print("\nVocê morreu! Fim de jogo.")

    return inimigos_mortos

#menu onde vc coloca as informações do oreia seca
def menu_batalha():
    print('\n--- Escolha seu personagem ---\n')

    personagem = escolher_ficha()

    if personagem is None:
        print("Nenhuma ficha válida selecionada.")
        return

    nome_personagem = personagem["nome"]
    classe_personagem = personagem["classe"]
    v_forca = personagem["forca"]
    v_magia = personagem["magia"]
    v_agilidade = personagem["agilidade"]

    poder_personagem = calculo_poder(v_forca, v_magia, v_agilidade)
    ranking_final = definir_ranking(poder_personagem)
    total_derrotados = sistema_batalha(poder_personagem, v_agilidade)

#relatório de desempenho na jornada do oreia seca
    print("\n" + "=" * 30)
    print("      RELATÓRIO FINAL")
    print("=" * 30)
    print(f"Nome: {nome_personagem}")
    print(f"Classe: {classe_personagem}")
    print(f"Poder Total: {poder_personagem}")
    print(f"Ranking: {ranking_final}")
    print(f"Inimigos Derrotados: {total_derrotados}")
    print("=" * 30)


menu()
