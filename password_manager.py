from cryptography.fernet import Fernet

class PasswordManager:
    @staticmethod
    def make_key():
        key = Fernet.generate_key()
        return key

    @staticmethod
    def encrypt(password, key):
        crypto = Fernet(key)
        return crypto.encrypt(password)

    @staticmethod
    def decrypt(password, key):
        if not isinstance(password, bytes):
            password = bytes(password, 'utf-8')
        crypto = Fernet(key)
        return str(crypto.decrypt(password)).strip("b' '")

if __name__ == "__main__":
    key = PasswordManager.make_key()
    pw = input('Enter your password: ')
    pw = bytes(pw, 'utf-8')
    e_pw = PasswordManager.encrypt(pw, key)

    print(f"E_KEY = {key}")
    print(f"EE = {e_pw}")


    