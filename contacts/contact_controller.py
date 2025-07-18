from agenda_1.find_dir import find_dir
from agenda_1.agendas.agenda_controller import agenda_dir

dir = agenda_dir()
def escolher_contato(agenda):  # Função de escolha de contato numa agenda e será usada nos comandos 4 e 5.
    with open(dir + agenda + '.txt',
              'r') as a:  # Abre arquivo da agenda, transforma numa lista ordenada alfabeticamente para exibir ao usuário.
        conteudo = a.read()
        a_list = sorted(list(conteudo.split(';')))
        a_list.remove('')
        for element in a_list:
            print(element)  # A escolha será do número ou do contato.
        contato = input('Escolha o nome ou o número do contato. \n')
    return contato