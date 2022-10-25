import string
from src.cypher import Cypher

class Vigenere(Cypher):
    def __init__(self, keyword):
        self.keyword = keyword
        self.alpha = string.ascii_lowercase
    
    def encrypt(self, message):
        encrypted_message = []
        for letter_index, letter in enumerate(message):
            letter_alpha_index = self.alpha.find(letter)
            keyword_alpha_index = self.alpha.find(self.keyword[letter_index % len(self.keyword)])
            encrypted_letter = self.alpha[(letter_alpha_index + keyword_alpha_index) % 26]
            encrypted_message.append(encrypted_letter)
        return ''.join(encrypted_message)

    def decrypt(self, encrypted_message):
        decrypted_message = []
        for letter_index, letter in enumerate(encrypted_message):
            letter_alpha_index = self.alpha.find(letter)
            keyword_alpha_index = self.alpha.find(self.keyword[letter_index % len(self.keyword)])
            decrypted_letter = self.alpha[(letter_alpha_index - keyword_alpha_index) % 26]
            decrypted_message.append(decrypted_letter)
        return ''.join(decrypted_message)

if __name__ == '__main__':
    cypher = Vigenere("super")
    print(cypher.encrypt("perasperaadastra"))
    print(cypher.decrypt("hygejhygervuhxis"))