import os
from hashlib import md5
from sys import exit
from time import sleep as espere

from modulos.gerenciador import Gerenciador
from modulos.registrador import *


# ----------------------------------------------------------------------------------------------------------------------
#                       Limpe a Tela
# ----------------------------------------------------------------------------------------------------------------------
def limpe_a_tela():
    """Função que realiza a limpeza do console em tempo de execução.

    :return: command(clear | cls)
    """
    os.system(command='cls') if os.name in ['nt', 'dos'] else os.system(command='clear')


# ----------------------------------------------------------------------------------------------------------------------
#                       Encerrar Programa
# ----------------------------------------------------------------------------------------------------------------------
def encerre_o_programa():
    """Função para encerramento do programa.

    :return: function(exit())
    """
    print('Encerrando.......')
    espere(1)
    return exit()


# ----------------------------------------------------------------------------------------------------------------------
#                       Cadastrar Cliente
# ----------------------------------------------------------------------------------------------------------------------
def realize_cadastro_do_cliente():
    """Função que processa a opção 'Cadastrar Cliente'
    do menu inicial.

    :return: str(mensagem)
    """
    limpe_a_tela()
    print(cadastro_do_cliente)
    cliente = Cliente(Registrador().colete_dados_cliente)
    nome_arquivo = md5(bytes(cliente.cpf, 'utf-8')).hexdigest()
    if Gerenciador(nome_arquivo).procure_arquivo():
        print(cliente_ja_cadastrado)
    else:
        conta = Conta(Registrador().colete_dados_conta)
        dados = {**cliente.dados_cliente, **conta.dados_conta}
        Gerenciador(nome_arquivo, dados, 'ext').escreva_arquivo_extrato('Abertura', f"a+ R${conta.disponivel:.2f}")
        print(Gerenciador(nome_arquivo, dados).escreva_arquivo_conta())
        Gerenciador(nome_arquivo).mostre_arquivo()
        espere(3)
        limpe_a_tela()


# ----------------------------------------------------------------------------------------------------------------------
#                       Operação em Conta
# ----------------------------------------------------------------------------------------------------------------------
def realize_operacao_em_conta():
    """Função que processa a opção 'Operação em Conta"
    do menu inicial.

    :return: str(mensagem)
    """
    chaves_cliente = ['nome', 'cpf', 'endereco', 'bairro']
    chaves_conta = ['saldo', 'credito']
    limpe_a_tela()
    print(operacoes_em_conta)
    documento = InputPadrao('Digite o CPF: ').conteudo
    nome_arquivo = md5(bytes(Documento(documento).cpf, 'utf-8')).hexdigest()
    if Documento(documento).checar and Gerenciador(nome_arquivo).procure_arquivo():
        limpe_a_tela()
        Gerenciador(nome_arquivo).mostre_arquivo()
        dados = Gerenciador(nome_arquivo).retire_dados_do_arquivo()
        cliente = Cliente(dict({d for d in dados.__items() if d[0] in chaves_cliente}))
        conta = Conta(dict({d for d in dados.__items() if d[0] in chaves_conta}))
        while True:
            operacao = Menu().menu_operacoes
            # ------------------------------------ Saque ---------------------------------------------------------------
            if operacao == 1:
                valor = InputPadrao('Digite o valor: ', float).conteudo
                if conta.sacar(valor):
                    dados = {**cliente.dados_cliente, **conta.dados_conta}
                    Gerenciador(nome_arquivo, dados, 'ext').escreva_arquivo_extrato("Saque", f"s- R${valor:.2f}")
                    Gerenciador(nome_arquivo, dados).escreva_arquivo_conta()
                    limpe_a_tela()
                else:
                    limpe_a_tela()
                    print(valor_excedeu_limite)
                Gerenciador(nome_arquivo).mostre_arquivo()
            # ------------------------------------ Depósito ------------------------------------------------------------
            elif operacao == 2:
                valor = InputPadrao('Digite o valor: ', float).conteudo
                conta.depositar(valor)
                dados = {**cliente.dados_cliente, **conta.dados_conta}
                Gerenciador(nome_arquivo, dados, 'ext').escreva_arquivo_extrato("Depósito", f"d+ R${valor:.2f}")
                Gerenciador(nome_arquivo, dados).escreva_arquivo_conta()
                limpe_a_tela()
                Gerenciador(nome_arquivo).mostre_arquivo()
            # ------------------------------------ Extrato -------------------------------------------------------------
            elif operacao == 3:
                limpe_a_tela()
                Gerenciador(nome_arquivo).escreva_arquivo_extrato("Extrato", "# simples consulta")
                Gerenciador(nome_arquivo).mostre_arquivo()
                Gerenciador(nome_arquivo, seletor='ext').mostre_arquivo()
            # ------------------------------------ Novo Crédito --------------------------------------------------------
            elif operacao == 4:
                valor = InputPadrao('Digite o novo Crédito: ', float).conteudo
                conta.credito = valor
                dados = {**cliente.dados_cliente, **conta.dados_conta}
                Gerenciador(nome_arquivo, dados, 'ext').escreva_arquivo_extrato('Novo Crédito', f"c+ R${valor:.2f}")
                Gerenciador(nome_arquivo, dados).escreva_arquivo_conta()
                limpe_a_tela()
                Gerenciador(nome_arquivo).mostre_arquivo()
            # ------------------------------------ Retornar ------------------------------------------------------------
            else:
                return limpe_a_tela()
    else:
        limpe_a_tela()
        print(cliente_nao_encontrado)


# ----------------------------------------------------------------------------------------------------------------------
#                       Execução do Programa
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    limpe_a_tela()
    print(abertura_do_programa)
    while True:
        print(sistema_de_cadastro_de_clientes)
        opcao = Menu().menu_inicial
        # Cadastrar Cliente
        if opcao == 1:
            realize_cadastro_do_cliente()
        # Operações em Conta
        elif opcao == 2:
            realize_operacao_em_conta()
        # Encerrar Programa
        else:
            encerre_o_programa()
