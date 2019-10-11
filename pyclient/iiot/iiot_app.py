import os
from iiot.iiot_client import IIoTCliente

DISTRIBUTION_NAME = 'iiot'
DEFAULT_URL = 'http://rest-api:8008'

def _get_keyfile(customerName):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.priv'.format(key_dir, customerName)

def _get_pubkeyfile(customerName):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.pub'.format(key_dir, customerName)

def setar_estado():
    cliente = input("Cliente: ")
    estado = input("Estado: ")
    arquivo_chave = _get_keyfile(cliente)
    iiot_cli = IIoTCliente(baseUrl=DEFAULT_URL, keyFile=arquivo_chave)
    resposta = iiot_cli.setar_estado(estado)
    print("Resposta: {}".format(resposta))

def obter_estado():
    cliente = input("Cliente: ")
    arquivo_chave = _get_keyfile(cliente)
    iiot_cli = IIoTCliente(baseUrl=DEFAULT_URL, keyFile=arquivo_chave)
    dados = iiot_cli.obter_estado()

    if dados is not None:
        print("\n{} tem um estado de = {}\n".format(cliente, dados.decode()))
    else:
        raise Exception("estados nao encontrados: {}".format(cliente))

def main():
    op = "-1"
    while op != "3":
        op = input("Opcao: ")
        if op == "1":
            setar_estado()
        elif op == "2":
            obter_estado()