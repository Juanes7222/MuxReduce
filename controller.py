import utils
import DATA as DT

def main(minterminos: str):
    DT.lista_binarios = convertir_a_binario(minterminos)
    DT.Agrupados = agrupar(DT.lista_binarios)
    variables, _ = utils.procesar_variables(minterminos)
    minterminos: list = utils.to_list(minterminos)
    minterminos = list(map(int, minterminos))
    minterminos.sort()
    resultado = reduccion(minterminos, variables)
    DT.Respuesta_final = resultado
    return resultado

def convertir_a_binario(minterms_str):
    minterms = list(map(int, minterms_str.split(',')))
    max_minterm = max(minterms) if minterms else 0
    num_bits = max_minterm.bit_length() if max_minterm > 0 else 1
    diccionario_binario = {}
    for i in range(2 ** num_bits):
        binario_lista = [int(bit) for bit in format(i, f'0{num_bits}b')]
        diccionario_binario[i] = binario_lista
    return diccionario_binario

def agrupar(diccionario_binario):
    grupos = {
        '0': [], 
        '1': []  
    }
    for clave, lista_bits in diccionario_binario.items():
        decimal = int("".join(map(str, lista_bits)), 2)  # Convierte la lista de bits a decimal
        if lista_bits[0] == 0: 
            grupos['0'].append(decimal)
        else:  
            grupos['1'].append(decimal)
    return grupos


def reduccion(minterminos: list, variables: list):
    cant_minterminos = 2**len(variables)

    resultado = []
    var_principal = variables[0]
    length = cant_minterminos//2
    for i, j in zip(range(length), range(length, cant_minterminos, 1)):
        if i in minterminos and j in minterminos:
            resultado.append(1)
        elif i in minterminos:
            resultado.append(f"{var_principal}'")
        elif j in minterminos:
            resultado.append(var_principal)
        else:
            resultado.append(0)
    return resultado

if __name__ == "__main__":
    minterms = "0,10,15"
    diccionario = convertir_a_binario(minterms) 
    print(diccionario)
    agrupados = agrupar(diccionario)
    print(agrupados)

    main(minterms)
