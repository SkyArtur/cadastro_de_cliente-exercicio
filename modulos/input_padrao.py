from modulos.mensagens import *


# ----------------------------------------------------------------------------------------------------------------------
#              Classe InputPadrao
# ----------------------------------------------------------------------------------------------------------------------
class InputPadrao:
    def __init__(self, input_usuario="=> ", tipo_input=None, minn=None, maxx=None):
        """Entrada de dados do programa.

        Construtor:

        Construtor da classe, disponibiliza o input para o usuário, pode controlar
        o tipo de input desejado (int, float, str), pode controlar a dimensão numérica
        dos menus (minn, maxx).

        __ini__()

        Operadores:

        __repr__(), __str__(), __len__(), __iter__(),
        __eq__(), __le__(), __lt__(), __ge__(), __gt__().

        Métodos:

        menu_input()
        cep_input()

        Privado:

        __meu_input()

        Properties:

        @conteudo

        :param input_usuario: Any
        :param tipo_input: int: int | float: float | str: None
        :param minn: int - menor opção de um menu.
        :param maxx: int - maior opção do menu.
        """
        self.__input_do_usuario = self.__meu_input(input_usuario, tipo_input)
        self.__min = minn
        self.__max = maxx

    def __repr__(self):
        return self.__input_do_usuario

    def __str__(self):
        return self.__input_do_usuario

    def __iter__(self):
        return iter(self.__input_do_usuario)

    def __len__(self):
        return len(self.__input_do_usuario)

    def __eq__(self, other):
        return self.__input_do_usuario == other

    def __ne__(self, other):
        return self.__input_do_usuario != other

    def __lt__(self, other):
        return self.__input_do_usuario < other

    def __le__(self, other):
        return self.__input_do_usuario <= other

    def __gt__(self, other):
        return self.__input_do_usuario > other

    def __ge__(self, other):
        return self.__input_do_usuario >= other

    @property
    def conteudo(self):
        """
        Getter da classe InputPadrao.

        :return: input do usuário -> int | float | str
        """
        return self.__input_do_usuario

    def __meu_input(self, input_usuario, tipo_input=None):
        """Função privada da classe InputPadrao. Faz o tratamento dos inputs do programa.

        :param input_usuario: Any
        :param tipo_input: int | float | str
        :return: input_usuario -> int | float | str
        """
        if tipo_input == int:
            while True:
                try:
                    self.__input_do_usuario = int(input(input_usuario))
                except ValueError:
                    print(msg_entrada_01)
                else:
                    return int(self.__input_do_usuario)
        elif tipo_input == float:
            while True:
                try:
                    self.__input_do_usuario = float(input(input_usuario))
                except ValueError:
                    print(msg_entrada_02)
                else:
                    return float(self.__input_do_usuario)
        else:
            while True:
                try:
                    self.__input_do_usuario = input(input_usuario)
                except ValueError:
                    print(msg_entrada_03)
                else:
                    return self.__input_do_usuario

    def menu_input(self):
        """Método para tratamento da entrada de opções em menus.

        :return: input_do_usuario -> int
        """
        while self.__input_do_usuario < self.__min or self.__input_do_usuario > self.__max:
            print(msg_entrada_04)
            self.__input_do_usuario = self.__meu_input('=> ', int)
        else:
            return int(self.__input_do_usuario)

    def cep_input(self):
        """Método para tratamento da entrada do CEP.

        :return: input_do_usuario -> str
        """
        while not len(self.__input_do_usuario) == 5 and not self.__input_do_usuario.isnumeric():
            print(msg_entrada_05)
            self.__input_do_usuario = self.__meu_input('=> ')
        else:
            return str(self.__input_do_usuario)


# ----------------------------------------------------------------------------------------------------------------------
#              Classe menu
# ----------------------------------------------------------------------------------------------------------------------
class Menu:
    """Classe para construção dos menus do programa.

    Propriedades:

    @menu_inicial,
    @menu_creditos,
    @menu_operacoes.
    """

    @property
    def menu_inicial(self):
        """Propriedade para construção do menu inicial do programa.

        :return: resposta_do_usuario -> int
        """
        resposta_do_usuario = InputPadrao(f'{msg_entrada_menu_01}\n=> ', int, 0, 3).menu_input()
        return resposta_do_usuario

    @property
    def menu_creditos(self):
        """Propriedade para construção do menu para definição dos créditos do usuário.

        :return: resposta_usuario -> int
        """
        resposta_usuario = InputPadrao(f'{msg_entrada_menu_02}\n=> ', int, 1, 2).menu_input()
        return resposta_usuario

    @property
    def menu_operacoes(self):
        """Propriedade para construção do menu para realização de operações em conta.

        :return: resposta_usuario -> int
        """
        resposta = InputPadrao(f'{msg_entrada_menu_03}\n=> ', int, 0, 4).menu_input()
        return resposta
