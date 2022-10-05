import string
from .caesar import Caesar

class CaesarWithKeyword(Caesar):
    def __init__(self, key, keyword):
        self.key = key
        alpha = string.ascii_lowercase
        self.alpha_with_keyword = "".join(dict.fromkeys(keyword + alpha))

    def encrypt(self, message):
        secret_alpha = self.alpha_with_keyword[self.key:] + self.alpha_with_keyword[:self.key]
        return self._encrypt(message, self.alpha_with_keyword, secret_alpha)

    def decrypt(self, encrypted_message):
        secret_alpha = self.alpha_with_keyword[-self.key:] + self.alpha_with_keyword[:-self.key]
        return self._encrypt(encrypted_message, self.alpha_with_keyword, secret_alpha)

if __name__ == '__main__':
    cypher = CaesarWithKeyword(5, 'lemon')
    print(cypher.encrypt("letmein"))
    print(cypher.decrypt("abycbrf"))
    