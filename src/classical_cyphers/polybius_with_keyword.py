import string
from src.cypher import Cypher

class PolybiusWithKeyword(Cypher):
    def __init__(self, keyword = ''):
        self.keyword = keyword
        self.secret_alpha = self._create_secret_alpha()

    def _create_secret_alpha(self):
        secret_alpha = []
        for character in self.keyword + string.ascii_lowercase:
            if character not in secret_alpha and character != "j":
                secret_alpha.append(character)
        secret_alpha = ''.join(secret_alpha)
        return secret_alpha

    def encrypt(self, message):
        message = message.replace('j', 'i')
        encrypted_message = []
        for letter in message:
            letter_new_index = self.secret_alpha.find(letter) + 1
            row, col = divmod(letter_new_index,5)
            if  (letter_new_index%5 == 0):
                encrypted_message.append(str(row)+str(col+5))
            else:
                encrypted_message.append(str(row+1)+str(col))
        return "".join(encrypted_message)

    def decrypt(self, encrypted_message):
        decrypted_message = []
        for i in range(0, len(encrypted_message), 2):
            row = int(encrypted_message[i])
            col = int(encrypted_message[i+1])
            letter = self.secret_alpha[(row-1)*5 + col-1]
            decrypted_message.append(letter)
        return "".join(decrypted_message)

if __name__ == '__main__':
    cypher = PolybiusWithKeyword('lemon')
    print(cypher.encrypt("whyareyourunning"))
    print(cypher.decrypt('52325421421254144542451515331531'))
    