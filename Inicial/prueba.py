import  re
"""def is_mail():
    email = input("Ingrese su email: ")
    resultado = re.search("@", email)
    if(resultado):
        print("Valido")
    else:
        print("No valido")
is_mail()"""

def is_mail():
    email = input("Ingrese su email: ")
    if "@" not in email:
        print("No Valido")
    else:
        print("valido")
is_mail()