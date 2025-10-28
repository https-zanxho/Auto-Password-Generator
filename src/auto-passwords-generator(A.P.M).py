import secrets
import string
import time

# Definimos la variable que define la longitud de la contraseña
password_lenght = 0
password_dictionary = {}

# Definiendo los caracteres permitidos en la contraseña
password_symbols = string.ascii_letters + string.digits + string.punctuation 
# bucle para validar la URL y que no este vacia
while True:
    name_or_url_for_password = input("Please provide the URL for the password(cant be empty): ").strip()
    if name_or_url_for_password:
        break
    print("The URL or name cannot be empty.")


# Bloque try para evitar que el usuario introduzca un caracter invalido y solo pueda meter numeros del 8 al 100
while True:
    try:
        password_lenght = int(input("Introduce the lenght of the password(8-100): "))
        if password_lenght > 100 or password_lenght < 8:
            print("select a valid lenght")
        else:
            print(f"Lenght set to {password_lenght}")
            break
    except ValueError:
        print("Please introduce a valid number")
time.sleep(1)

# Generamos la contraseña según la opción seleccionada
secure_password = ''.join(secrets.choice(password_symbols) for i in range(password_lenght))

#Agregamos la contraseña a un diccionario con el formato URL:PASSWORD
password_dictionary[name_or_url_for_password] = secure_password

# Imprimimos la contraseña generada
print("The password is being generated please wait...")
time.sleep(3)
print(f"the secure password is: {secure_password}")

print(password_dictionary)
# Pausa para evitar que el programa se cierre inmediatamente
input("\nPress any key to close the program...")