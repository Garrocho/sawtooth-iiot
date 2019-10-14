import os
from iot.iot_client import IoTClient

DISTRIBUTION_NAME = 'iot'
DEFAULT_URL = 'http://rest-api:8008'

def _get_keyfile(customerName):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.priv'.format(key_dir, customerName)

def _get_pubkeyfile(customerName):
    home = os.path.expanduser("~")
    key_dir = os.path.join(home, ".sawtooth", "keys")
    return '{}/{}.pub'.format(key_dir, customerName)

def store_sensor_data():
    client = input("Client: ")
    state = input("State: ")
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    response = iot_cli.store_sensor_data(state)
    print("Response: {}".format(response))

def get_sensor_data():
    client = input("Client: ")
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_data()

    if data is not None:
        print("\n{} have a state = {}\n".format(client, data.decode()))
    else:
        raise Exception("state not found: {}".format(client))

def get_sensor_history():
    client = input("Client: ")
    key_file = _get_keyfile(client)
    iot_cli = IoTClient(baseUrl=DEFAULT_URL, keyFile=key_file)
    data = iot_cli.get_sensor_history()

    if data is not None:
        for i in data:
            print(i.decode())
    else:
        raise Exception("history not found: {}".format(client))

def main():
    op = "-1"
    while op != "4":
        print("\n1 - store sensor data\n2 - get sensor data\n3 - get sensor history\n4 - exit\n")
        op = input("Operation: ")
        if op == "1":
            store_sensor_data()
        elif op == "2":
            get_sensor_data()
        elif op == "3":
            get_sensor_history()