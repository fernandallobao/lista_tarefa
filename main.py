#Crie um programa em que o usuário possa cadastrar uma lista de tarefas a fazer no dia. Após terminar, envie o link do repositório no GitHub.
tarefas = []

while True:
    print('\n')
    print('Bem vindo a sua lista de tarefa: ')
    print('1 - para inserir tarefa.')
    print('2 - para sair.')

    op = input('Digite o numero da opção desejada: ')

    match op:
        case '1':
            nova_tarefa = input('Informe a tarefa: ').capitalize()
            tarefas.append(nova_tarefa)
            print('\n')
            print('Esses sãos as tarefas que voce digitou:')
            for tarefa in tarefas:
                print(f'- {tarefa}.')
        case '2':
            break
        case _: 
            print('Opção inválida.')