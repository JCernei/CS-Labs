from src.symetrical_cyphers.block.constants import *
from src.symetrical_cyphers.utils import *
from src.cypher import Cypher

class Des(Cypher):
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

    def round(self, input, key, num):
        left = input[0:8]
        temp = input[8:16]
        right = temp
        temp = self.transpose(EP, temp)
        temp = xor(temp, key)
        temp = self.sbox_substitute(temp)
        temp = self.transpose(P, temp)
        left = xor(left, temp)
        return right + left

    def encrypt(self, message, key):
        keys = self.get_keys(key)
        # initial transpose
        message = self.transpose(IP, message)
        # perform 16 rounds
        for i in range(16):
            message = self.round(message, keys[i], i)
        # swap 2 halves 32-bits of the message
        message = message[8:16] + message[0:8]
        # perform the final transpose
        message = self.transpose(IP1, message)
        return message

    def decrypt(self, message, key):
        keys = self.get_keys(key)
        message = self.transpose(IP, message)
        # perform reverse 16-rounds
        for i in range(15, -1, -1):
            message = self.round(message, keys[i], 15 - i)
        message = message[8:16] + message[0:8]
        message = self.transpose(IP1, message)
        return message


if __name__ == '__main__':
    message = b'I am Ion'.hex()
    key = 'AABB09182736C11D'
    cipher = Des()
    
    encrypted_message = cipher.encrypt(message, key)
    print(hex_to_bin(encrypted_message))
    # 0001111101001110001100100000001100110000011101001110101100110111

    decrypted_message = cipher.decrypt(encrypted_message, key)
    print(bytes.fromhex(decrypted_message).decode('utf-8'))
    # I am Ion
