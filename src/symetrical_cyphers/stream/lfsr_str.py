from src.symetrical_cyphers.utils import to_bits, from_bits
from src.symetrical_cyphers.stream.lfsr import Lfsr


class LfsrStr(Lfsr):
    def __init__(self, register, taps):
        super().__init__(register, taps)

    def generate_key(self, key_length):
        self.register = self.origin.copy()
        key = []
        for i in range(key_length):
            key.append(self._generate_key_bit())
        return key

    def process_bits(self, message):
        key = self.generate_key(len(message))
        processed_bits = []
        for i in range(len(message)):
            processed_bits.append(message[i] ^ key[i])
        return processed_bits

    def encrypt(self, message):
        return self.process_bits(message)

    def decrypt(self, encrypted_message):
        return self.process_bits(encrypted_message)


if __name__ == '__main__':

    cypher = LfsrStr(register=[0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0,
                                1, 0, 0, 0, 1, 0, 0, 0, 0], taps=[16, 2])

    message = to_bits('Who am I')

    encrypted_message = cypher.encrypt(message)
    print(''.join(map(str, encrypted_message)))
    # 0011111100111001011010111001111100001110110001111100101011001100

    decrypted_message = cypher.decrypt(encrypted_message)
    print(from_bits(decrypted_message))
    # Who am I
