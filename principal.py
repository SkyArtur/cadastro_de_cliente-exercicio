import os
from hashlib import md5
from sys import exit
from time import sleep

from modulos.gerenciador import Gerenciador
from modulos.registrador import *


# ----------------------------------------------------------------------------------------------------------------------
#                       Limpar Tela
# ----------------------------------------------------------------------------------------------------------------------
def limpar_tela():
    """Função que realiza a limpeza do console em tempo de execução.

    :return: command(clear | cls)
    """
    os.system(command='cls') if os.name in ['nt', 'dos'] else os.system(command='clear')


# ----------------------------------------------------------------------------------------------------------------------
#                       Encerrar Programa
# ----------------------------------------------------------------------------------------------------------------------
def encerrar():
    """Função para encerramento do programa.

    :return: function(exit())
    """
    print('Encerrando.......')
    sleep(1.5)
    return exit()


# ----------------------------------------------------------------------------------------------------------------------
#                       Cadastrar Cliente
# ----------------------------------------------------------------------------------------------------------------------
def cadastrar_cliente():
    """Função que processa a opção 'Cadastrar Cliente'
    do menu inicial.

    :return: str(mensagem)
    """
    limpar_tela()
    print(forma2)
    cliente = Cliente(Registro().registrar_cliente)
    nome_arquivo = md5(bytes(cliente.cpf, 'utf-8')).hexdigest()
    if Gerenciador(nome_arquivo).procurar():
        print(msg_principal_01)
    else:
        conta = Conta(Registro().registrar_conta)
        dados_principais = {**cliente.dados_cliente, **conta.dados_conta}
        Gerenciador(nome_arquivo, dados_principais, 'ext').escrever_extrato('Abertura', f"a+ R${conta.disponivel:.2f}")
        print(Gerenciador(nome_arquivo, dados_principais).escrever_conta())
        Gerenciador(nome_arquivo).visualizar()
        sleep(2)
        limpar_tela()


# ----------------------------------------------------------------------------------------------------------------------
#                       Operação em Conta
# ----------------------------------------------------------------------------------------------------------------------
def operacao_em_conta():
    """Função que processa a opção 'Operação em Conta"
    do menu inicial.

    :return: str(mensagem)
    """
    cliente, conta = 0, 0
    ref_cliente = ['nome', 'cpf', 'endereco', 'bairro']
    ref_conta = ['saldo', 'credito']
    limpar_tela()
    print(forma3)
    documento = InputPadrao('Digite o CPF: ').conteudo
    nome_arquivo = md5(bytes(Documento(documento).cpf, 'utf-8')).hexdigest()
    if Documento(documento).checar and Gerenciador(nome_arquivo).procurar():
        limpar_tela()
        Gerenciador(nome_arquivo).visualizar()
        dados_principais = Gerenciador(nome_arquivo).extrair_dados()
        cliente = Cliente(dict({d for d in dados_principais.items() if d[0] in ref_cliente}))
        conta = Conta(dict({d for d in dados_principais.items() if d[0] in ref_conta}))
        while True:
            op = Menu().menu_operacoes
            # ------------------------------------ Saque ---------------------------------------------------------------
            if op == 1:
                valor = InputPadrao('Digite o valor: ', float).conteudo
                if conta.sacar(valor):
                    dados_principais = {**cliente.dados_cliente, **conta.dados_conta}
                    Gerenciador(nome_arquivo, dados_principais, 'ext').escrever_extrato("Saque", f"s- R${valor:.2f}")
                    Gerenciador(nome_arquivo, dados_principais).escrever_conta()
                    limpar_tela()
                else:
                    limpar_tela()
                    print(msg_principal_03)
                Gerenciador(nome_arquivo).visualizar()
            # ------------------------------------ Depósito ------------------------------------------------------------
            elif op == 2:
                valor = InputPadrao('Digite o valor: ', float).conteudo
                conta.depositar(valor)
                dados_principais = {**cliente.dados_cliente, **conta.dados_conta}
                Gerenciador(nome_arquivo, dados_principais, 'ext').escrever_extrato("Depósito", f"d+ R${valor:.2f}")
                Gerenciador(nome_arquivo, dados_principais).escrever_conta()
                limpar_tela()
                Gerenciador(nome_arquivo).visualizar()
            # ------------------------------------ Extrato -------------------------------------------------------------
            elif op == 3:
                limpar_tela()
                Gerenciador(nome_arquivo).escrever_extrato("Extrato", "# simples consulta")
                Gerenciador(nome_arquivo).visualizar()
                Gerenciador(nome_arquivo, seletor='ext').visualizar()
            # ------------------------------------ Novo Crédito --------------------------------------------------------
            elif op == 4:
                valor = InputPadrao('Digite o novo Crédito: ', float).conteudo
                conta.credito = valor
                dados_principais = {**cliente.dados_cliente, **conta.dados_conta}
                Gerenciador(nome_arquivo, dados_principais, 'ext').escrever_extrato('Novo Crédito', f"c+ R${valor:.2f}")
                Gerenciador(nome_arquivo, dados_principais).escrever_conta()
                limpar_tela()
                Gerenciador(nome_arquivo).visualizar()
            # ------------------------------------ Retornar ------------------------------------------------------------
            else:
                return limpar_tela()
    else:
        limpar_tela()
        print(msg_principal_02)


# ----------------------------------------------------------------------------------------------------------------------
#                       Execução do Programa
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    limpar_tela()
    print(abertura)
    while True:
        print(forma1)
        opcao = Menu().menu_inicial
        # Cadastrar Cliente
        if opcao == 1:
            cadastrar_cliente()
        # Operações em Conta
        elif opcao == 2:
            operacao_em_conta()
        # Encerrar Programa
        else:
            encerrar()
