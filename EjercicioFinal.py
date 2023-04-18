"""
Se desarrolla individualmente y se entrega hasta antes de las 14:00 horas al correo pvalenciam@uni.pe
    - Defina en listas los números de cuentas y saldos de los ahorros de clientes de una institución bancaria
    - Defina funciones que permitan actualizar y consultar el saldo de una cuenta de las listas
    - El programa debe mostrar las cuentas y sus saldos correspondientes, para luego elegir una cuenta, indicar el tipo de actualización a realizar y mostrar el saldo actualizado.
    - La ejecución se repite hasta que se ingrese como numero de cuenta -1
Entregar en un documento en formato docx el código en texto (no imagen) y las capturas de pantalla de la ejecución.
en un documento en formato docx el código en texto (no imagen) y las capturas de pantalla de la ejecución.
"""

# DEFINIMOS LISTA
cuentas = [
    [
        '0011-0284-0200555555555',
        1000
    ],
    [
        '0011-0284-0200666666666',
        2000
    ],
    [
        '0011-0284-0200777777777',
        3000
    ]
]

# FUNCIONES
# Determinamos si existe cuenta
def consultar_cuenta(cuenta_elegida, cuentas):
    for value in cuentas:
        if cuenta_elegida == value[0]:
            return [True, value]
    return [False]

# Actualizamos cuenta:
def actualizar_cuenta(cuenta_elegida, cuentas, accion_elegida, monto):
    if accion_elegida == "retirar":
        for value in cuentas:
            if cuenta_elegida == value[0]:
                if monto > value[1]: # Validacion de importe a retirar
                    result = [False, "No tienes saldo suficiente"]
                else:
                    value[1] -= monto
                    result = [True, "Retiro realizado correctamente", value[1]]

    elif accion_elegida == "depositar":
        for value in cuentas:
            if cuenta_elegida == value[0]:
                value[1] += monto
                result = [True, "Deposito realizado correctamente", value[1]]
    else:
        result = [False, "No se ingreso accion correcta"]

    return result

cuenta_elegida = ""
while cuenta_elegida != "-1":
    # LISTAMOS CUENTAS
    print("\n---- CUENTAS DISPONIBLES ----")
    for value in cuentas:
        print("\n***********************************************")
        print("Cuenta: " + value[0])
        print("Saldo: " + str(value[1]))
        print("***********************************************")

    # ELEGIMOS PRODUCTO
    cuenta_elegida = input("\nElige cuenta ('-1' para finalizar): ")

    # DETENEMOS SI ESCRIBE FINAL
    if cuenta_elegida == "-1":
        exit()

    # VALIDAMOS EXISTENCIA DE CUENTA
    consultar = consultar_cuenta(cuenta_elegida, cuentas)
    if consultar[0] == True:
        # OBTENEMOS INFORMACION DE CUENTA
        nro_cuenta = consultar[1][0]
        saldo_cuenta = consultar[1][1]

        # MOSTRAMOS ACCIONES DISPONIBLES
        print("""
        Cuenta disponible, dispone de estas acciones:
        - Retirar (retirar)
        - Depositar (depositar)
        """)

        # ELEGIMOS ACCION
        accion_elegida = input("Elige accion: ")
        monto_ingresado = int(input("Ingrese monto: "))

        # EJECUTAMOS ACTUALIZACION
        actualizar = actualizar_cuenta(cuenta_elegida, cuentas, accion_elegida, monto_ingresado)

        # RESPUESTA DE ACTUALIZACION
        print("\n---- RESPUESTA DE SOLICITUD ----")
        print("\n***********************************************")
        if (actualizar[0] == True): # Se realizo la actualizacion
            print("Mensaje: " + actualizar[1])
            print("Cuenta: " + nro_cuenta)
            print("Saldo actualizado: " + str(actualizar[2]))
        else:
            print("Mensaje: " + actualizar[1])
            print("Cuenta: " + nro_cuenta)
            print("Saldo: " + str(saldo_cuenta))
        print("***********************************************")
    else:
        print("\nNo se encontro cuenta, eliga una cuenta que exista...")
        continue
