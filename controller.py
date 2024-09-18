import utils

def main(minterminos: str):
    variables, _ = utils.procesar_variables(minterminos)
    minterminos: list = utils.to_list(minterminos)
    minterminos = list(map(int, minterminos))
    minterminos.sort()
    resultado = reduccion(minterminos, variables)
    print(resultado)

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
    main("0,3,4,5,6,7,9,10,12")