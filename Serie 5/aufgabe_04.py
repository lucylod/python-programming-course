from hashlib import sha256

def tresor(code):
    secret_code = ("b2b2f104d32c638903e151a9b20d6e27"
                   "b41d8c0c84cf8458738f83ca2f1dd744")

    m = sha256()
    m.update(code.encode())

    if m.hexdigest() == secret_code:
        print("Tresor geöffnet! Code ist:", code)
        return True
    else:
        print("Falscher Code:", code)
        return False

if __name__ == "__main__":
    user_code = input("Gib den 4-stelligen Tresorcode ein: ")
    tresor(user_code)
