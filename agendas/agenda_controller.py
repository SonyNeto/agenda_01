from agenda_1.find_dir import find_dir

def agenda_dir():
    return find_dir(__file__)

def escolher_agenda():  # Função de escolha de agenda na lista de agendas e será usada nos comandos 1, 3, 4 e 5.
    dir = agenda_dir()
    with open(dir + 'lista_agendas.txt', 'r') as a:
        conteudo = a.read()
        a_list = sorted(list(conteudo.split(';')))
        a_list.remove('')
        for element in a_list:
            print(str(a_list.index(element) + 1) + '. ' + element)  # A escolha será pelo número exibido.
        numero_agenda = input('Escolha uma agenda. \n')
    return a_list[int(numero_agenda) - 1]