from sympy import gcd
from src.cypher import Cypher


class Rsa(Cypher):
    def __init__(self, p, q):
        self.public_key, self.private_key, self.n = self.generate_keypair(p, q)

    def generate_keypair(self, p, q):
        n = p * q
        phi = (p-1) * (q-1)

        for e in range(phi, 0, -1):
            if gcd(e, phi) == 1:
                break

        d = pow(e, -1, phi)
        return (e, d, n)

    def encrypt(self, message):
        e = self.public_key
        encrypted_message = []
        for character in message:
            ascii_value = ord(character)
            encrypted_character = pow(ascii_value, e) % self.n
            encrypted_message.append(encrypted_character)
        return encrypted_message

    def decrypt(self, encrypted_message):
        d = self.private_key
        decrypted_message = []
        for character in encrypted_message:
            ascii_value = pow(character, d) % self.n
            decrypted_character = chr(ascii_value)
            decrypted_message.append(decrypted_character)
        return decrypted_message


if __name__ == '__main__':
    cypher = Rsa(421, 691)
    message = ('you shall not pass')

    encrypted_message = cypher.encrypt(message)
    print("".join(str(s) for s in encrypted_message))

    decrypted_message = cypher.decrypt(encrypted_message)
    print("".join(str(s) for s in decrypted_message))
