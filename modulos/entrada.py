class MeuInput:
    def __init__(self, input_usuario="~| ", tipo_input=None, minn=None, maxx=None):
        self.__input_do_usuario = self.__meu_input(input_usuario, tipo_input)
        self.__min = minn
        self.__max = maxx

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
        return self.__input_do_usuario

    def __meu_input(self, input_usuario, tipo_input):
        msg1 = f'''ErroEntrada ~01:
        São aceitos apenas números inteiros.'''
        msg2 = f'''ErroEntrada ~02:
        Não são aceitos letras ou caractéres especiais.
        Use o ponto(.) ao invés da vírgula(,) para separar
        casas decimais.'''
        msg3 = f'''ErroEntrada ~03:
        Parece que você digitou algo errado!'''
        if tipo_input == int:
            while True:
                try:
                    self.__input_do_usuario = int(input(input_usuario))
                except ValueError:
                    print(msg1)
                else:
                    return int(self.__input_do_usuario)
        elif tipo_input == float:
            while True:
                try:
                    self.__input_do_usuario = float(input(input_usuario))
                except ValueError:
                    print(msg1)
                else:
                    return float(self.__input_do_usuario)
        else:
            while True:
                try:
                    self.__input_do_usuario = input(input_usuario)
                except ValueError:
                    print(msg1)
                else:
                    return self.__input_do_usuario

    def menu_input(self):
        msg = f'''InputMenuError ~01:
        Parece que você digitou uma opção inválida!!'''
        while self.__input_do_usuario < self.__min or self.__input_do_usuario > self.__max:
            print(msg)
            self.__input_do_usuario = self.__meu_input('=> ', int)
        else:
            return self.__input_do_usuario
