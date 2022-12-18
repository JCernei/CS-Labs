from src.cyphers.symetrical_cyphers.block.constants import *
from src.cyphers.symetrical_cyphers.utils import *
from src.cyphers.cypher import Cypher


class Des(Cypher):
    def __init__(self, key):
        self.key = key

    # permutate input
    def transpose(self, sequence, input):
        output = ""
        input = hex_to_bin(input)
        for i in range(len(sequence)):
            output += input[sequence[i] - 1]
        output = bin_to_hex(output)
        return output

    def sbox_substitute(self, input):
        output = ""
        input = hex_to_bin(input)
        for i in range(0, 48, 6):
            temp = input[i: i + 6]
            num = i // 6
            row = int(temp[0] + temp[5], 2)
            col = int(temp[1:5], 2)
            output += str(int(hex(S_BOX[num][row][col]), 16))
        return output

    # left Circular Shifting bits
    def left_circular_shift(self, input, numBits):
        n = len(input) * 4
        perm = list(range(2, n+1))
        perm.append(1)
        while (numBits > 0):
            numBits = numBits-1
            input = self.transpose(perm, input)
        return input

    # preparing 16 keys for 16 rounds
    def get_keys(self, key):
        keys = []
        # first key permutation
        key = self.transpose(PC1, key)
        for i in range(16):
            key = self.left_circular_shift(
                key[0:7], SHIFT_BITS[i]) + self.left_circular_shift(key[7:14], SHIFT_BITS[i])
            # second key permutation
            keys.append(self.transpose(PC2, key))
        return keys

    def round(self, input, key):
        left = input[0:8]
        temp = input[8:16]
        right = temp
        temp = self.transpose(EP, temp)
        temp = xor(temp, key)
        temp = self.sbox_substitute(temp)
        temp = self.transpose(P, temp)
        left = xor(left, temp)
        return right + left

    def encrypt(self, message):
        message = bytes(message, encoding='utf-8').hex()
        keys = self.get_keys(self.key)
        # initial transpose
        message = self.transpose(IP, message)
        # perform 16 rounds
        for i in range(16):
            message = self.round(message, keys[i])
        # swap 2 halves 32-bits of the message
        message = message[8:16] + message[0:8]
        # perform the final transpose
        message = self.transpose(IP1, message)
        return hex_to_bin(message)

    def decrypt(self, message):
        message = bin_to_hex(message)
        keys = self.get_keys(self.key)
        message = self.transpose(IP, message)
        # perform reverse 16-rounds
        for i in range(15, -1, -1):
            message = self.round(message, keys[i])
        message = message[8:16] + message[0:8]
        message = self.transpose(IP1, message)
        return bytes.fromhex(message).decode('utf-8')


if __name__ == '__main__':
    message = b'I am Ion'.hex()
    cipher = Des(key='AABB09182736C11D')

    encrypted_message = cipher.encrypt(message)
    print(hex_to_bin(encrypted_message))
    # 0001111101001110001100100000001100110000011101001110101100110111

    decrypted_message = cipher.decrypt(encrypted_message)
    print(bytes.fromhex(decrypted_message).decode('utf-8'))
    # I am Ion
