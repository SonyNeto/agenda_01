from agenda_1.agendas.agenda_controller import escolher_agenda, agenda_dir
from agenda_1.contacts.contact_controller import escolher_contato

dir = agenda_dir()

def exibir_agenda():
    agenda_escolhida = escolher_agenda()  # Usa a função escolher_agenda() para o usuário selecionar uma agenda na lista de agendas.
    path = dir + agenda_escolhida + '.txt'  # Abre o arquivo correspondente à agenda escolhida.
    with open(path,
              'r') as p:  # Interpreta o arquivo, dividindo a string contida numa tupla de listas com os nomes e números dos contatos.
        p = sorted(tuple(p.read().split(';')))
        p.remove('')
        for element in p:
            print(element)  # Exibe a agenda.

def criar_agenda():
    nome = input('Digite um nome para a agenda: ')
    open(dir + nome + '.txt', 'x')
    with open(dir + 'lista_agendas.txt', 'a') as a:
        a.write(
            nome + ';')  # Cria um arquivo .txt com o nome da agenda e adiciona este nome escolhido na lista de agendas
        # separando-o dos demais com um ';'.

def inserir_contato():
    agenda_escolhida = escolher_agenda()  # Usa a função escolher_agenda() para o usuário selecionar uma agenda na lista de agendas.
    path = dir + agenda_escolhida + '.txt'
    contato = input('Digite o nome do contato: ')
    numero = input('Digite o numero do contato: ')
    with open(path, 'a') as p:
        p.write(
            contato + ': ' + numero + ';')  # Escreve no arquivo .txt da agenda selecionada o nome e número do contato, separados por :,
        # e separando este conjunto dos demais com um ';'.

def modificar_contato():
    agenda_escolhida = escolher_agenda()  # Usa a função escolher_agenda() para o usuário selecionar uma agenda na lista de agendas.
    path = dir + agenda_escolhida + '.txt'
    contato = escolher_contato(agenda_escolhida)  # Usa a função escolher_contato() para o usuário selecionar um contato na agenda escolhida.
    with open(path,
              'r') as p:  # Interpreta o arquivo, dividindo a string contida numa tupla de listas com os nomes e números dos contatos.
        conteudo = p.read()
        p_tuple = sorted(tuple(conteudo.split(';')))
        for element in p_tuple:  # Encontra o elemento(lista) da tupla que contém o contato selecionado.
            e = element.split(': ')
            if contato in e:
                comando_modificar = input('O que desejas modificar?\n'
                                          '1. Nome do contato\n'
                                          '2. Número do contato\n')
                # Subscreve o elemento da lista que foi modificado na string lida inicialmente pelo interpretador.
                if comando_modificar == '1':
                    novo_nome = input('Digite o novo nome: ')
                    modificado = conteudo.replace(e[0], novo_nome)
                elif comando_modificar == '2':
                    novo_numero = input('Digite o novo numero: ')
                    modificado = conteudo.replace(e[1], novo_numero)
    with open(path,
              'w') as nova_agenda:  # Subscreve o conteúdo do arquivo da agenda pela nova string modificada, que contém todos os outros contatos inalterados mais a modificação.
        nova_agenda.write(modificado)

def excluir_contato():
    # Este comando funciona da mesma forma que o 4, mas modifica a string inicial com uma string vazia, que equivale a excluir o contato.
    agenda_escolhida = escolher_agenda()
    path = dir + agenda_escolhida + '.txt'
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