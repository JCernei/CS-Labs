import unittest
from src.symetrical_cyphers.utils import *
from src.symetrical_cyphers.stream.lfsr_str import LfsrStr
from src.symetrical_cyphers.block.des import Des
from src.symetrical_cyphers.block.constants import *


class TestSymetricalCyphers(unittest.TestCase):
    def test_lfsr(self):
        cypher = LfsrStr(register=[0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0,
                                   1, 0, 0, 0, 1, 0, 0, 0, 0], taps=[16, 2])

        message = to_bits('Who am I')
        encrypted_message = cypher.encrypt(message)
        decrypted_message = cypher.decrypt(encrypted_message)

        assert ''.join(map(str, encrypted_message)
                       ) == '0011111100111001011010111001111100001110110001111100101011001100'

        assert from_bits(decrypted_message) == 'Who am I'

    def test_des(self):
        cypher = Des(key='AABB09182736C11D')

        message = b'I am Ion'.hex()
        encrypted_message = cypher.encrypt(message)
        decrypted_message = cypher.decrypt(encrypted_message)

        assert hex_to_bin(
            encrypted_message) == "0001111101001110001100100000001100110000011101001110101100110111"

        assert bytes.fromhex(decrypted_message).decode('utf-8') == "I am Ion"


if __name__ == '__main__':
    unittest.main()
