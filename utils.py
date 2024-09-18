import re
from string import ascii_uppercase


def validar_pesos(pesos):
    match = re.match(r"^\s*(?:\d+,\s*)*(?:\d+)\s*$", pesos)
    if match:
        return True
    return False


def obtener_cant_vars(pesos):
    ultimo_peso = int(pesos[-1])
    cant_variables = len(bin(ultimo_peso)) - 2
    return cant_variables


def procesar_variables(pesos: str, cant = None):

    match = validar_pesos(pesos)
    if not match:
        return None, None
    pesos = to_list(pesos)
    pesos.sort(key=int)
    if not cant:
        cant_variables = obtener_cant_vars(pesos)
    else:
        cant_variables = int(cant)
    variables = list(ascii_uppercase[:cant_variables])
    return variables, cant_variables


def to_list(str_: str):
    return str_.strip().split(",")


def number_to_binary(number: int | str, length=4):
    if isinstance(number, str):
        if "0x" in number:
            number = int(number, 16)
    binary = int(number).to_bytes(length=4, signed=True)
    normal_binary = ''.join(format(byte, '08b') for byte in binary)
    return normal_binary[-length:]
