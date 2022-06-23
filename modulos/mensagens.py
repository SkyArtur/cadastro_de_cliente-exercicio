"""
Módulo que armazena as mensagens impressas pelo programa.
"""

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo principal
# ----------------------------------------------------------------------------------------------------------------------
abertura_do_programa = '''Exercício prático no aprendizado em Python.
Copyright (c) 2022 - Ponta Grossa/PR. 
Projeto Cadastro de Cliente.
Artur dos Santos Shon - EAD - UNINTER - 2021.'''
sistema_de_cadastro_de_clientes = '''------------------------------------------
     Sistema de Cadastro de Clientes
------------------------------------------'''
cadastro_do_cliente = '''------------------------------------------
            Cadastro do Cliente
------------------------------------------'''
operacoes_em_conta = '''------------------------------------------
           Operações em Conta
------------------------------------------'''
msg_principal_01 = '''ErroCadastro ~01:
    Cliente já cadastrado!
'''
msg_principal_02 = '''ErroCadastro ~03:
    Cliente não encontrado!
'''
msg_principal_03 = '''ErroLimite ~01:
    O valor de saque excede seu limite disponível
'''

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo registrador
# ----------------------------------------------------------------------------------------------------------------------
msg_registrador_01 = """ErroDocumento ~01:
    Número do documento não é válido!
"""
msg_registrador_02 = """ErroCep ~01:
    número de CEP inválido!
"""
msg_registrador_03 = """MensagemCep ~01:
    Endereço encontrado!
"""

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo gerenciador
# ----------------------------------------------------------------------------------------------------------------------
msg_gerenciador_01 = """MensagemGerente ~01:
    Arquivo do cliente criado com sucesso.
"""
msg_gerenciador_02 = """MensagemGerente ~02:
    Arquivo do cliente atualizado com sucesso.
"""
msg_gerenciador_03 = f"""MensagemGerente ~03:
    Arquivo não encontrado.
"""

# ----------------------------------------------------------------------------------------------------------------------
#              Mensagens do módulo entrada
# ----------------------------------------------------------------------------------------------------------------------
msg_entrada_01 = f'''ErroEntrada ~01:
    São aceitos apenas números inteiros.
'''
msg_entrada_02 = f'''ErroEntrada ~02:
    Não são aceitos letras ou caractéres especiais.
    Use o ponto(.) ao invés da vírgula(,) para separar
    casas decimais.
'''
msg_entrada_03 = f'''ErroEntrada ~03:
    Parece que você digitou algo errado!
'''
msg_entrada_04 = f'''InputMenuError ~01:
    Parece que você digitou uma opção inválida!!
'''
msg_entrada_05 = f'''InputCepError ~01:
    Parece que você digitou algo inválido.
    Por favor, digite apenas os números.
'''
msg_entrada_menu_01 = """Menu Inicial:
    [1] Cadastrar Novo Cliente
    [2] Operações em Conta
    [0] Encerrar"""
msg_entrada_menu_02 = """Deseja definir os créditos do cliente?
    [1] Sim
    [2] Não"""
msg_entrada_menu_03 = """Qual operação deseja realizar?
    [1] Sacar
    [2] Depositar
    [3] Consultar extrato
    [4] Novo Crédito
    [0] Retornar"""
