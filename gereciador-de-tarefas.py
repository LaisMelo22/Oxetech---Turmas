tarefas = []

def adicionar_tarefa(descricao):
    """Adiciona uma nova tarefa a lista."""
    nova_tarefa = {
        'descricao': descricao,
        'completa': False
    }
    tarefas.append(nova_tarefa)
    print(f"\n[OK] Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas, mostrando seu status (completa ou pendente)."""
    if not tarefas:
        print("\n[INFO] Nenhuma tarefa na lista ainda.")
        return

    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas):
        # APLICADO: Remocao de acentos e emojis. Usa [C] para Completa e [P] para Pendente.
        status = "[C]" if tarefa['completa'] else "[P]"
        # Mostra o indice da tarefa para que o usuario possa interagir com ela
        print(f"[{i + 1}] {status} {tarefa['descricao']}")
    print("------------------------")

def completar_tarefa(indice):
    """Marca uma tarefa como completa com base no seu indice (mostrado na lista)."""
    try:
        # O usuario ve o indice a partir de 1, entao ajustamos para o indice da lista (comeca em 0)
        indice_real = int(indice) - 1
        
        if 0 <= indice_real < len(tarefas):
            tarefas[indice_real]['completa'] = True
            print(f"\n[SUCESSO] Tarefa '{tarefas[indice_real]['descricao']}' marcada como COMPLETA!")
        else:
            print("\n[ERRO] Indice de tarefa invalido.")
            
    except ValueError:
        print("\n[ERRO] Por favor, insira um numero valido para o indice.")

def exibir_menu():
    """Exibe o menu de opcoes para o usuario."""
    print("\n=== Gerenciador de Tarefas ===")
    print("[1] Adicionar nova tarefa")
    print("[2] Listar todas as tarefas")
    print("[3] Marcar tarefa como completa")
    print("[4] Sair")
    print("==============================")
    
def iniciar_gerenciador():
    """Funcao principal para rodar o gerenciador de tarefas."""
    
    # Laco principal do programa para manter o menu rodando ate que o usuario escolha sair
    while True:
        exibir_menu()
        
        # Uso de try-except para lidar com entradas nao numericas
        try:
            escolha = input("Escolha uma opcao: ")
        except EOFError: # Lida com finalizacao abrupta (como em alguns ambientes web)
             break

        if escolha == '1':
            descricao = input("Digite a descricao da nova tarefa: ")
            if descricao:
                adicionar_tarefa(descricao)
            else:
                # APLICADO: Remocao de acentos
                print("\n[AVISO] A descricao da tarefa nao pode ser vazia.")
                
        elif escolha == '2':
            listar_tarefas()
            
        elif escolha == '3':
            listar_tarefas()
            if tarefas:
                # APLICADO: Remocao de acentos
                indice = input("Digite o NUMERO da tarefa que deseja completar: ")
                completar_tarefa(indice)
                
        elif escolha == '4':
            # APLICADO: Remocao de acentos
            print("\n[FIM] Gerenciador de tarefas encerrado. Ate mais!")
            break
            
        else:
            # APLICADO: Remocao de acentos
            print("\n[AVISO] Opcao invalida. Por favor, escolha um numero de 1 a 4.")

# Chama a funcao principal para iniciar o programa
if __name__ == "__main__":
    iniciar_gerenciador()