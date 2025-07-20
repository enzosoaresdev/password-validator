#Password Validator.

def check_length(password):
    """Verifica se a senha tem pelo menos 8 caracteres."""
    if len(password) >= 8:
        return True
    return False

def has_uppercase(password):
    """Verifica se a senha contém pelo menos uma letra maiúscula."""
    for char in password:
        if char.isupper():
            return True
    return False

def has_lowercase(password):
    """Verifica se a senha contém pelo menos uma letra minúscula."""
    for char in password:
        if char.islower():
            return True
    return False

def has_digit(password):
    """Verifica se a senha contém pelo menos um digito(número)."""
    for char in password:
        if char.isdigit():
            return True
    return False

def classify_password(password):
    """Classifica a senha, conforme todas verificações forem verdadeiras."""
    if(
        check_length(password) and
        has_uppercase(password) and
        has_lowercase(password) and
        has_digit(password)
    ):
        return "Senha forte!"
    return "Senha fraca, tente novamente!"

password_corret = False

while not password_corret:
    password = input("Digite sua senha: ")
    result = classify_password(password)
    print(result)
    if result == "Senha forte!":
        password_corret = True