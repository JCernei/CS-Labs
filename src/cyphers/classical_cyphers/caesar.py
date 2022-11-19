import string
from src.cyphers.cypher import Cypher

class Caesar(Cypher):
    def __init__(self, key):
        self.key = key
        self.alpha = string.ascii_lowercase

    def _encrypt(self, message, alpha, secret_alpha):
        encrypted_message = []
        for letter in message:
            encrypted_letter = secret_alpha[alpha.find(letter)]
            encrypted_message.append(encrypted_letter)
        return ''.join(encrypted_message)

    def encrypt(self, message):
        secret_alpha = self.alpha[self.key:] + self.alpha[:self.key]
        return self._encrypt(message, self.alpha, secret_alpha)

    def decrypt(self, encrypted_message):
        secret_alpha = self.alpha[-self.key:] + self.alpha[:-self.key]
        return self._encrypt(encrypted_message, self.alpha, secret_alpha)

if __name__ == '__main__':
    cypher = Caesar(5)
    print(cypher.encrypt("anothersecretmessage"))
    print(cypher.decrypt("fstymjwxjhwjyrjxxflj"))
