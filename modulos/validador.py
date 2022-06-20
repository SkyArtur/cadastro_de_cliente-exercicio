class CPF:
    def __init__(self, documento):
        self.__cpf = documento
        self.__cpf_form = f"{self.__cpf[:3]}.{self.__cpf[3:6]}." \
                          f"{self.__cpf[6:9]}-{self.__cpf[9:]}"

    def __str__(self):
        return self.__cpf_form

    @property
    def cpf(self):
        return self.__cpf_form

    @property
    def validar(self):
        d1, d2 = 0, 0
        for i, j in enumerate(range(10, 1, -1)):
            d1 += int(self.__cpf[i]) * j
        d1 = 11 - (d1 % 11)
        d1 = 0 if d1 > 9 else d1
        for i, j in enumerate(range(11, 1, -1)):
            d2 += int(self.__cpf[i]) * j
        d2 = 11 - (d2 % 11)
        d2 = 0 if d2 > 9 else d2
        if f"{d1}{d2}" in self.__cpf:
            return True
        else:
            return False


class Documento(CPF):
    def __init__(self, documento):
        super().__init__(documento)
        self.__doc = documento
        self.__msg = "Número do documento não é válido!"

    @property
    def checar(self):
        if len(self.__doc) < 12:
            if CPF(self.__doc).validar:
                return True
            else:
                print(self.__msg)
                return False
