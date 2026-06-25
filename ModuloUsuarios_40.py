# Base de Datos

usuarios_list = []

# Validaciones


def validar_sexo(sexo):
    if sexo in ["M", "F"]:
        return True
    else:
        print("Error, el sexo ingresado no es valido.")
        return False


def validar_password(password):
    if len(password.strip()) < 8:
        print("")
        return False

    tiene_numero = False
    for letra in password:
        if letra.isnumeric():
            tiene_numero = True

    tiene_letra = False
    for letra in password:
        if letra.isalpha():
            tiene_letra = True

    if " " in password:
        print("Error, la contraseña no puede tener espacio.")
        return False

    return tiene_numero and tiene_letra


def imprimir_usuario(usuario):
    print(f"""
    ------- Usuario -------      
    |Nombre del Usuario : {usuario["Nombre"]}
    |Sexo : {usuario["Sexo"]}
    |Password : {usuario["Password"]}
    -----------------------""")


# Transacciones
