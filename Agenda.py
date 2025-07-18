#O programa de agendas permite o controle de várias agendas. Pode-se criar agendas distintas
#e dentro de cada uma, contatos com seus nomes e números correspondentes.
#É possível visualizar cada agenda individualmente e modificar ou excluir contatos.

#Uma agenda é um arquivo .txt com uma string contendo o nome e o número, nesta ordem, de cada contato
#na ordem em que foi inserido, separados por um ';'.
#Ao ler uma agenda, o programa divide essa string numa tupla com uma lista de dois elementos, o nome e o número,
#para cada contato e ordena alfabeticamente.
#Os nomes das agendas também são separados num arquivo .txt paralelo contendo uma string
#que é interpretada no programa como uma lista e exibe ao usuário as agendas para sua escolha.
def agenda():
    comando = 0         #Estado "neutro" do comando(botão) a ser dado.
    arq_main = __file__ #Path do script
    dir_main = '\\'.join(arq_main.split('\\')[:-1]) + '\\' #Diretório do script
    while comando != '6': #O último comando (6) é para Sair. Enquanto não for executado, o programa de agendas estará funcionando.
        comando = input ('Digite o número correspondente ao que desejas executar: \n'
                         '1. Exibir uma agenda existente\n'
                         '2. Criar uma nova agenda\n'
                         '3. Inserir um contato numa agenda existente\n'
                         '4. Modificar um contato de uma agenda existente\n'
                         '5. Excluir um contato de uma agenda existente\n'
                         '6. Sair\n')
        def escolher_contato(agenda): #Função de escolha de contato numa agenda e será usada nos comandos 4 e 5.
            with open(dir_main + agenda + '.txt', 'r') as a: #Abre arquivo da agenda, transforma numa lista ordenada alfabeticamente para exibir ao usuário.
                conteudo = a.read()
                a_list = sorted(list(conteudo.split(';')))
                a_list.remove('')
                for element in a_list:
                    print(element) #A escolha será do número ou do contato.
                contato = input('Escolha o nome ou o número do contato. \n')
            return contato
        def escolher_agenda(): #Função de escolha de agenda na lista de agendas e será usada nos comandos 1, 3, 4 e 5.
            with open(dir_main + 'lista_agendas.txt', 'r') as a:
                conteudo = a.read()
                a_list = sorted(list(conteudo.split(';')))
                a_list.remove('')
                for element in a_list:
                    print(str(a_list.index(element) + 1) + '. ' + element) #A escolha será pelo número exibido.
                numero_agenda = input('Escolha uma agenda. \n')
            return a_list[int(numero_agenda) - 1]

        if comando == '1': #Comando 1: Exibir uma agenda.
            agenda_escolhida = escolher_agenda() #Usa a função escolher_agenda() para o usuário selecionar uma agenda na lista de agendas.
            path = dir_main + agenda_escolhida + '.txt' #Abre o arquivo correspondente à agenda escolhida.
            with open(path, 'r') as p: #Interpreta o arquivo, dividindo a string contida numa tupla de listas com os nomes e números dos contatos.
                p = sorted(tuple(p.read().split(';')))
                p.remove('')
                for element in p:
                    print(element) #Exibe a agenda.

        if comando == '2': #Comando 2: Criar uma agenda.
            nome = input('Digite um nome para a agenda: ')
            open(dir_main + nome + '.txt', 'x')
            with open(dir_main + 'lista_agendas.txt', 'a') as a:
                a.write(nome + ';') #Cria um arquivo .txt com o nome da agenda e adiciona este nome escolhido na lista de agendas
                #separando-o dos demais com um ';'.

        if comando == '3': #Comando 3: Inserir contato numa agenda.
            agenda_escolhida = escolher_agenda() #Usa a função escolher_agenda() para o usuário selecionar uma agenda na lista de agendas.
            path = dir_main + agenda_escolhida + '.txt'
            contato = input('Digite o nome do contato: ')
            numero = input('Digite o numero do contato: ')
            with open(path, 'a') as p:
                p.write(contato + ': ' + numero + ';') #Escreve no arquivo .txt da agenda selecionada o nome e número do contato, separados por :,
                # e separando este conjunto dos demais com um ';'.

        if comando == '4': #Comando 4: Modificar um contato numa agenda.
            agenda_escolhida = escolher_agenda() #Usa a função escolher_agenda() para o usuário selecionar uma agenda na lista de agendas.
            path = dir_main + agenda_escolhida + '.txt'
            contato = escolher_contato(agenda_escolhida) #Usa a função escolher_contato() para o usuário selecionar um contato na agenda escolhida.
            with open(path, 'r') as p: #Interpreta o arquivo, dividindo a string contida numa tupla de listas com os nomes e números dos contatos.
                conteudo = p.read()
                p_tuple = sorted(tuple(conteudo.split(';')))
                for element in p_tuple: #Encontra o elemento(lista) da tupla que contém o contato selecionado.
                    e = element.split(': ')
                    if contato in e:
                        comando_modificar = input('O que desejas modificar?\n'
                                             '1. Nome do contato\n'
                                             '2. Número do contato\n')
                        #Subscreve o elemento da lista que foi modificado na string lida inicialmente pelo interpretador.
                        if comando_modificar == '1':
                            novo_nome = input('Digite o novo nome: ')
                            modificado = conteudo.replace(e[0], novo_nome)
                        elif comando_modificar == '2':
                            novo_numero = input('Digite o novo numero: ')
                            modificado = conteudo.replace(e[1], novo_numero)

            with open(path, 'w') as nova_agenda: #Subscreve o conteúdo do arquivo da agenda pela nova string modificada, que contém todos os outros contatos inalterados mais a modificação.
                nova_agenda.write(modificado)

        if comando == '5': #Comando 5: Excluir um contato.
            #Este comando funciona da mesma forma que o 4, mas modifica a string inicial com uma string vazia, que equivale a excluir o contato.
            agenda_escolhida = escolher_agenda()
            path = dir_main + agenda_escolhida + '.txt'
            contato = escolher_contato(agenda_escolhida)
            with open(path, 'r') as p:
                conteudo = p.read()
                p_tuple = sorted(tuple(conteudo.split(';')))
                for element in p_tuple:
                    e = element.split(': ')
                    if contato in e:
                        modificado = conteudo.replace(str(element) + ';', '')
            with open(path, 'w') as nova_agenda:
                nova_agenda.write(modificado)
    print('Até mais! Encerrando programa.')
if __name__ == '__main__':
    agenda()