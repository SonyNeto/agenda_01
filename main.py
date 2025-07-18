#O programa de agendas permite o controle de várias agendas. Pode-se criar agendas distintas
#e dentro de cada uma, contatos com seus nomes e números correspondentes.
#É possível visualizar cada agenda individualmente e modificar ou excluir contatos.
from agenda_1.commands.commands import exibir_agenda, criar_agenda, inserir_contato, modificar_contato, excluir_contato


#Uma agenda é um arquivo .txt com uma string contendo o nome e o número, nesta ordem, de cada contato
#na ordem em que foi inserido, separados por um ';'.
#Ao ler uma agenda, o programa divide essa string numa tupla com uma lista de dois elementos, o nome e o número,
#para cada contato e ordena alfabeticamente.
#Os nomes das agendas também são separados num arquivo .txt paralelo contendo uma string
#que é interpretada no programa como uma lista e exibe ao usuário as agendas para sua escolha.
def agenda():
    comando = 0           #Estado "neutro" do comando(botão) a ser dado.
    while comando != '6': #O último comando (6) é para Sair. Enquanto não for executado, o programa de agendas estará funcionando.
        comando = input ('Digite o número correspondente ao que desejas executar: \n'
                         '1. Exibir uma agenda existente\n'
                         '2. Criar uma nova agenda\n'
                         '3. Inserir um contato numa agenda existente\n'
                         '4. Modificar um contato de uma agenda existente\n'
                         '5. Excluir um contato de uma agenda existente\n'
                         '6. Sair\n')

        if comando == '1': #Comando 1: Exibir uma agenda.
            exibir_agenda()

        if comando == '2': #Comando 2: Criar uma agenda.
            criar_agenda()

        if comando == '3': #Comando 3: Inserir contato numa agenda.
            inserir_contato()

        if comando == '4': #Comando 4: Modificar um contato numa agenda.
            modificar_contato()

        if comando == '5': #Comando 5: Excluir um contato.
            excluir_contato()

    print('Até mais! Encerrando programa.')
if __name__ == '__main__':
    agenda()